<div align=center>

# discord-ext-ipcx

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

## Resources

- [Documentation](https://discord-ext-ipcx.readthedocs.io)
- [Examples](https://github.com/No767/discord-ext-ipcx/tree/main/examples)

## Motivation and differences

I forked and upgraded the discord-ext-ipc library to now work with discord.py v2 or higher. The primary reason why is that most of the "IPC" libraries out there are slow and I desperately needed a better IPC library for myself. The core has been kept almost intact, but here are some the changes worth noting:

- The `start` method is now an coroutine and needs to be awaited.
- Actually type hinting the library

More in the future may be added or deleted.