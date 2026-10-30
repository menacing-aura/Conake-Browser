# Conake Browser v0.1.17 — Site Shield

Keep your place.

- Website pop-ups are blocked by default instead of becoming new active tabs.
- Open **Site Shield** beside the address bar to see the blocked count, review an address, or change the current site's pop-up and redirect rules.
- **Guard Cross-site Redirects** blocks top-level page jumps and replacements to another site. It is enabled by default for **enma.lol** and its subdomains; other sites can opt in through the shield menu.
- The guard also blocks ordinary links leaving that site. Explicit address-bar navigation and **Open Link in New Tab** remain available, and embedded frames can still load.
- A reviewed pop-up or context-menu link remembers the tab that opened it. Back uses normal page history first, then returns to that original tab when there is no history. If you closed the source, Conake reopens its address.
- Site rules stay in your encrypted local account. Blocked-address history stays in memory and resets on leaving the site, locking, or exiting.
- Anime window controls, fullscreen, Tab Studio, extensions, and offline Snake Run remain included.

This update controls pop-ups and top-level redirects. Some in-page ads or content inside embedded frames may remain. Closed-page form and playback state cannot be recovered by reopening an address.

74 automated checks and Linux desktop checks use local fixtures to verify pop-up blocking, script and HTTP redirects, embedded frames, source-tab Back, preserved drafts, normal navigation, and encrypted rule restoration.

Close Conake before updating, install the package for your computer, then sign in. Verify hashes with SHA256SUMS.txt.

[Community](https://discord.gg/BMcST6NaZS) · [Donate](https://cash.app/$one1aura) · Collaborations: godscripters@gmail.com
