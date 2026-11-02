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

