Examples
========

Here are some ways you can use this library in your own bot. Make sure to adjust it to your own bot's needs.
If you wish to run these examples locally, please install the examples extras via ``python3 -m pip install discord-ext-ipcx[examples]``.
For GitHub based examples, please see the `examples directory <https://github.com/No767/discord-ext-ipcx/tree/main/examples>`_

Basic IPC
---------

``examples/basic/bot.py``
^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/basic/bot.py
   :language: python


``examples/basic/webserver.py``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/basic/webserver.py
   :language: python

Cog-based IPC
-------------

``examples/cog-based/cogs/__init__.py``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(This is to automatically load the cogs)

.. literalinclude:: ../examples/cog-based/cogs/__init__.py
   :language: python


``examples/cog-based/cogs/ipc.py``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/cog-based/cogs/ipc.py
   :language: python


``examples/cog-based/bot.py``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/cog-based/bot.py
   :language: python


``examples/cog-based/webserver.py``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/cog-based/webserver.py
   :language: python


FastAPI
-------

``examples/fastapi/bot.py``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/fastapi/bot.py
   :language: python


``examples/fastapi/webserver.py``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../examples/fastapi/webserver.py
   :language: python