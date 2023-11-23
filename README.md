<div align=center>

# discord-ext-ipcx

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/discord-ext-ipcx?logo=python&logoColor=white&label=Python)](https://pypi.org/project/discord-ext-ipcx/) [![CodeQL](https://github.com/No767/discord-ext-ipcx/actions/workflows/codeql.yml/badge.svg)](https://github.com/No767/discord-ext-ipcx/actions/workflows/codeql.yml) [![Build and Publish](https://github.com/No767/discord-ext-ipcx/actions/workflows/publish.yml/badge.svg)](https://github.com/No767/discord-ext-ipcx/actions/workflows/publish.yml) [![Lint](https://github.com/No767/discord-ext-ipcx/actions/workflows/lint.yml/badge.svg)](https://github.com/No767/discord-ext-ipcx/actions/workflows/lint.yml) [![PyPI - License](https://img.shields.io/pypi/l/discord-ext-ipcx?logo=github&logoColor=white&label=License)](https://github.com/No767/discord-ext-ipcx/blob/main/LICENSE) [![PyPI - Version](https://img.shields.io/pypi/v/discord-ext-ipcx?logo=pypi&logoColor=white&label=Version&link=https%3A%2F%2Fpypi.org%2Fproject%2Fdiscord-ext-ipcx%2F)](https://pypi.org/project/discord-ext-ipcx/)

An maintained discord.py extension for inter-process communication

<div align=left>

## Installation

**Python 3.8 or higher is required**

To install the library, you can just run the following command:

```bash
# On Linux/MacOS
python3 -m pip install discord-ext-ipcx

# On Windows
py -m pip install discord-ext-ipcx
```

To install the development version, do the following:

```bash
$ git clone https://github.com/No767/discord-ext-ipcx
$ cd discord-ext-ipcx
$ python3 -m pip install -U .
```

## Resources

- [Documentation](https://discord-ext-ipcx.readthedocs.io)
- [Examples](https://github.com/No767/discord-ext-ipcx/tree/main/examples)

## Motivation and differences

I forked and upgraded the discord-ext-ipc library to now work with discord.py v2 or higher. The primary reason why is that most of the "IPC" libraries out there are slow and I desperately needed a better IPC library for myself. The core has been kept almost intact, but here are some the changes worth noting:

- The `start` method is now an coroutine and needs to be awaited.
- Actually type hinting the library

More in the future may be added or deleted.