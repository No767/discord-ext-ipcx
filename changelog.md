## discord-ext-ipcx [0.4.0](https://github.com/No767/discord-ext-ipcx/tree/0.4.0) - 2024-12-09

### Features

- Implement `async with x` operations for `discord.ext.ipcx.Client` ([#56](https://github.com/No767/discord-ext-ipcx/issues/56))

### Removals and backward incompatible breaking changes

- Delist `discord.ext.ipcx.Client.get_port` from public methods ([#60](https://github.com/No767/discord-ext-ipcx/issues/60))

### Improved documentation

- Add FastAPI examples ([#57](https://github.com/No767/discord-ext-ipcx/issues/57))
- Modern library examples ([#59](https://github.com/No767/discord-ext-ipcx/issues/59))
- Include exceptions within API reference ([#61](https://github.com/No767/discord-ext-ipcx/issues/61))
- Add note about installation of example extras dependencies ([#62](https://github.com/No767/discord-ext-ipcx/issues/62))

### Miscellaneous internal changes

- Rename examples directories ([#58](https://github.com/No767/discord-ext-ipcx/issues/58))


## discord-ext-ipcx [0.3.0](https://github.com/No767/discord-ext-ipcx/tree/0.3.0) - 2024-11-22

### Bug fixes

- Fix missing return statements on server request handlers ([#48](https://github.com/No767/discord-ext-ipcx/issues/48))
- Remove unnecessary imports within `__init__.py` module ([#54](https://github.com/No767/discord-ext-ipcx/issues/54))

### Features

- Add Python 3.13 support ([#47](https://github.com/No767/discord-ext-ipcx/issues/47))
- Migrate to [Towncrier](https://towncrier.readthedocs.io/en/stable/index.html) ([#53](https://github.com/No767/discord-ext-ipcx/issues/53))

### Removals and backward incompatible breaking changes

- Entirely drop Python 3.8 support ([#44](https://github.com/No767/discord-ext-ipcx/issues/44))

### Improved documentation

- Modernize and improve front-facing documentation ([#49](https://github.com/No767/discord-ext-ipcx/issues/49))
- Remove unnecessary RTD configuration options ([#50](https://github.com/No767/discord-ext-ipcx/issues/50))

### Miscellaneous internal changes

- Migrate Dependabot to weekly scans and allow for grouped updates ([#51](https://github.com/No767/discord-ext-ipcx/issues/51))
