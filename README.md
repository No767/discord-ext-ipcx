<div align=center>

# discord-ext-ipcx

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/discord-ext-ipcx?logo=python&logoColor=white&label=Python)](https://pypi.org/project/discord-ext-ipcx/) [![CodeQL](https://github.com/No767/discord-ext-ipcx/actions/workflows/codeql.yml/badge.svg)](https://github.com/No767/discord-ext-ipcx/actions/workflows/codeql.yml) [![Build and Publish](https://github.com/No767/discord-ext-ipcx/actions/workflows/build_and_publish.yml/badge.svg)](https://github.com/No767/discord-ext-ipcx/actions/workflows/build_and_publish.yml) [![Lint](https://github.com/No767/discord-ext-ipcx/actions/workflows/lint.yml/badge.svg)](https://github.com/No767/discord-ext-ipcx/actions/workflows/lint.yml) [![PyPI - License](https://img.shields.io/pypi/l/discord-ext-ipcx?logo=github&logoColor=white&label=License)](https://github.com/No767/discord-ext-ipcx/blob/main/LICENSE) [![PyPI - Version](https://img.shields.io/pypi/v/discord-ext-ipcx?logo=pypi&logoColor=white&label=Version&link=https%3A%2F%2Fpypi.org%2Fproject%2Fdiscord-ext-ipcx%2F)](https://pypi.org/project/discord-ext-ipcx/)

An maintained discord.py extension for inter-process communication

<div align=left>

## Installation

**Python 3.9 or higher is required**

To install the library, you can just run the following command:

```bash
# On Linux/MacOS
python3 -m pip install discord-ext-ipcx

# On Windows
py -m pip install discord-ext-ipcx
```

To install the development version, do the following:

```bash
git clone https://github.com/No767/discord-ext-ipcx
cd discord-ext-ipcx
python3 -m pip install -U .
```

## Resources

- [Documentation](https://discord-ext-ipcx.readthedocs.io/en/stable)
- [Examples](https://github.com/No767/discord-ext-ipcx/tree/main/examples)

## Motivation and differences

Originally, I forked and upgraded the discord-ext-ipc library to work with discord.py v2 for my own needs. Alternative libraries were soon either left unmaintained or archived due to various reasons. This forked version aims to maintain support for newer versions of discord.py while keeping the core intact for easy migration. In the future, more may be added or deleted, but this is unlikely to happen.

Nonetheless, some modifications had to be made. Here are some changes worth noting:

- The `start` method is now an coroutine and needs to be awaited.

