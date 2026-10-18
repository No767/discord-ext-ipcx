# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "discord-ext-ipcx"
copyright = "2024-Present, No767"
author = "No767"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


intersphinx_mapping = {
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
    "python": ("https://docs.python.org/3", None),
    "discord": ("https://discordpy.readthedocs.io/en/latest", None),
}

_PY_CLASS = "py:class"

nitpick_ignore = {
    (_PY_CLASS, "aiohttp.web_request.Request"),
    (_PY_CLASS, "aiohttp.web_ws.WebSocketResponse"),
    (_PY_CLASS, "discord.ext.ipcx.client._T"),
    (_PY_CLASS, "discord.ext.ipcx.server._T"),
    (_PY_CLASS, "discord.ext.ipcx.server.RouteFunc"),
    (_PY_CLASS, "_P"),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = []

html_theme_options = {
    "dark_css_variables": {
        "color-brand-primary": "#c2b3ff",
        "color-brand-content": "#c2b3ff",
    },
    "light_css_variables": {
        "color-brand-primary": "#7c5cff",
        "color-brand-content": "#7c5cff",
    },
}
