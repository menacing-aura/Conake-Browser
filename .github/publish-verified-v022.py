"""Publish only approved desktop v0.2.2 installer bytes from the release transfer."""
import concurrent.futures
import hashlib
import http.client
import json
import os
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import quote

repo = os.environ['GITHUB_REPOSITORY']
assert repo == 'menacing-aura/Conake-Browser'
tag = 'v0.2.2'
target = os.environ['CONAKE_PUBLIC_TARGET']
mirror = 'https://conake-v022-installer-transfer.web-one1aura.workers.dev/v0.2.2/'
spec = json.loads(Path('.github/v022-digests.json').read_text())
filenames = {'conake-browser_0.2.2_amd64.deb','ConakeBrowser-0.2.2-linux-x86_64.AppImage',
             'ConakeBrowser-0.2.2-win-x64.exe','ConakeBrowser-0.2.2-mac-arm64.dmg',
             'ConakeBrowser-0.2.2-mac-x64.dmg','SHA256SUMS.txt'}
assert set(spec) == filenames
def api(path, method='GET', payload=None):
    args = ['gh','api','--method',method,'repos/'+repo+'/'+path]
    if payload is not None: args.extend(['--input','-'])
    data = json.dumps(payload).encode() if payload is not None else None
    return json.loads(subprocess.check_output(args,input=data))
def verified(asset, name):
    return asset['name'] == name and asset['size'] == spec[name]['size'] and asset['digest'] == 'sha256:'+spec[name]['sha256']
matches = [r for r in api('releases?per_page=100') if r['tag_name'] == tag]
assert len(matches) <= 1
if matches:
    release = matches[0]
    assert release['target_commitish'] == target and not release['prerelease']
    if not release['draft']:
        assert set(a['name'] for a in release['assets']) == filenames
        assert all(verified(a,a['name']) for a in release['assets'])
        print('The verified desktop release is already public.')
        raise SystemExit(0)
with tempfile.TemporaryDirectory() as temp:
    directory = Path(temp)
    def download(name):
        path = directory/name
        subprocess.run(['curl','--proto','=https','--fail','--silent','--show-error','--retry','3','--connect-timeout','20','--max-time','420','--output',str(path),mirror+quote(name)],check=True)
        assert path.stat().st_size == spec[name]['size'], name
        with path.open('rb') as f: digest = hashlib.file_digest(f,'sha256').hexdigest()
        assert digest == spec[name]['sha256'], name
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(download,sorted(filenames)))
    checks = (directory/'SHA256SUMS.txt').read_text().splitlines()
    assert sorted(checks) == sorted(spec[n]['sha256']+'  '+n for n in filenames-{'SHA256SUMS.txt'})
    print('All five installers matched their original sizes and SHA-256 checksums.')
    if not matches:
        release=api('releases','POST',{'tag_name':tag,'target_commitish':target,'name':'Conake Browser v0.2.2','draft':True,
            'body':Path('.github/v022-release-notes.md').read_text()})
    rid=release['id']
    existing={a['name']:a for a in release['assets']}
    assert set(existing)<=filenames
    def upload(name):
        if name in existing:
            assert verified(existing[name],name)
            return
        connection=http.client.HTTPSConnection('uploads.github.com',timeout=360)
        try:
            headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'User-Agent':'Conake-Studio-release',
                     'Content-Type':'application/octet-stream','Content-Length':str(spec[name]['size']),
                     'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}
            with (directory/name).open('rb') as f:
                connection.request('POST',f'/repos/{repo}/releases/{rid}/assets?name={quote(name)}',body=f,headers=headers)
                res=connection.getresponse()
                assert res.status==201, (name,res.status)
                assert verified(json.load(res),name),name
        finally: connection.close()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(upload,sorted(filenames)))
    final=api(f'releases/{rid}')
    assert final['draft'] and final['tag_name']==tag and final['target_commitish']==target
    assert {a['name'] for a in final['assets']}==filenames and all(verified(a,a['name']) for a in final['assets'])
    published=api(f'releases/{rid}','PATCH',{'draft':False,'make_latest':'true'})
    assert not published['draft'] and published['tag_name']==tag
    print('Published',published['html_url'])
