## v0.1.22 Linux preview · tab performance and website controls

**[Download the Linux .deb](https://github.com/menacing-aura/Conake-Browser/releases/download/v0.1.22/conake-browser_0.1.22_amd64.deb)** · **[Download the AppImage](https://github.com/menacing-aura/Conake-Browser/releases/download/v0.1.22/ConakeBrowser-0.1.22-linux-x86_64.AppImage)** · [Release notes](https://github.com/menacing-aura/Conake-Browser/releases/tag/v0.1.22) · [Linux checksums](https://github.com/menacing-aura/Conake-Browser/releases/download/v0.1.22/Conake-0.1.22-checksums.txt)

- Switching tabs preserves page surfaces and drafts, skips unchanged native bounds and avoids broadcasting full history/download records to every internal page.
- Hover or focus a tab for approximate renderer RAM. Shared renderer processes are labelled; GPU memory and separate subframes are excluded. Samples are taken on demand.
- Open **Settings → Websites & developer tools → Allow JavaScript on websites**. Saving a change reloads open websites and preserves navigation history. Conake's own pages remain interactive; some websites need scripts for login or video.
- Use **right-click → Inspect**, **View → Inspect Page**, **F12** or **Ctrl/Command+Shift+I** to open the current website's DevTools.

Close Conake before updating. Verify these two Linux installers using **Conake-0.1.22-checksums.txt**. Public Windows and macOS downloads remain v0.1.20; Chromebook Preview 06 is a separate, unchanged Android edition.

---

## v0.1.21 previews · Chrome Web Store browsing

**[Download the Linux .deb preview](https://github.com/menacing-aura/Conake-Browser/releases/download/v0.1.21/conake-browser_0.1.21_amd64.deb)** · [Linux release notes](https://github.com/menacing-aura/Conake-Browser/releases/tag/v0.1.21) · [Linux checksum](https://github.com/menacing-aura/Conake-Browser/releases/download/v0.1.21/SHA256SUMS.txt)

The Linux preview adds Chrome Web Store browsing and reviewed imports of unpacked Manifest V3 content-script extensions. Imports support one JavaScript file and one CSS file; background services and direct Chrome Web Store / CRX installation are not supported. Windows, macOS and AppImage downloads remain v0.1.20.

**[Download Chromebook Preview 06](https://github.com/menacing-aura/Conake-Browser/releases/download/v0.1.21-chromebook.6/ConakeBrowser-Chromebook-0.1.21-preview6.apk)** · [Chromebook installation instructions](https://github.com/menacing-aura/Conake-Browser/releases/tag/v0.1.21-chromebook.6) · [APK checksum](https://github.com/menacing-aura/Conake-Browser/releases/download/v0.1.21-chromebook.6/SHA256SUMS.txt)

Preview 06 adds a Chrome Web Store menu entry for browsing only, with an explanation that Android extension installation is unsupported. It retains the upper address-bar fixes, Go button, setup guide and Chromebook-only policy. Keep app data with `adb install -r ConakeBrowser-Chromebook-0.1.21-preview6.apk`. The existing 48-hour public-IP phone restriction remains.

---

## Chromebook Preview 05 · address-bar fix

The upper URL/search bar now submits with physical Enter, numpad Enter and on-screen Go, Search or Done. A visible **Go** button is also available. The top bar and new-tab search use the selected search engine.

[Get the signed Chromebook update and installation instructions](https://github.com/menacing-aura/Conake-Browser/releases/tag/v0.1.20-chromebook.5). Keep app data with `adb install -r ConakeBrowser-Chromebook-0.1.20-preview5.apk`; do not uninstall first. The existing Chromebook-only policy remains, including the 48-hour public-IP ban if opened on a phone.

Desktop v0.1.20 is unchanged.

---

Your first arc starts here.

- Open the new **Quick setup** card on a new tab, or **Navigate → Setup Guide**. The desktop guide is bundled and works offline; it explains installation, profiles, Conake Names, customization, tabs, fullscreen and Snake Run.
- Choose a color theme and search engine from the guide. Preferences and the dismissed setup reminder stay in the encrypted local profile.
- The desktop unlock screen now identifies the local profile clearly, shows password length and Caps Lock feedback, supports showing confirmation text, and links to setup and online Conake sign-in.
- **Conake Account for Names** has a dedicated sign-in page. Existing Names credentials still work. New accounts and recovery confirm the password before submitting.
- Choose a session-only sign-in (up to 12 hours) or a remembered seven-day sign-in. Review active sign-ins, sign out other sessions using the current password, and change the online password.
- Online password changes and account recovery rotate the recovery code and revoke older sessions. Copy or download the private code and store it safely.

The online Conake account manages .conake names. Desktop profile passwords and Extension Store accounts remain separate. There is no cloud sync or online password reset for the encrypted desktop profile. Google sign-in is not configured; no Google authentication is advertised.

Close Conake before updating and verify your installer with SHA256SUMS.txt.

[Setup guide](https://conake-domains.web-one1aura.workers.dev/setup) · [Conake Account](https://conake-domains.web-one1aura.workers.dev/account) · [Community](https://discord.gg/BMcST6NaZS)

© 2026 Conake Studios

