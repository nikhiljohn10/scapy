"""Sphinx configuration."""

import os
import sys
from datetime import datetime

from importlib_metadata import metadata

sys.path.insert(0, os.path.abspath(".."))
_DISTRIBUTION_METADATA = metadata("scapy-man")

project = "Scapy Manager"
author = _DISTRIBUTION_METADATA["Author"]
version = _DISTRIBUTION_METADATA["Version"]
copyright = f"{datetime.now().year}, {author}"


extensions = [
    "recommonmark",
    "sphinx_click",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
coverage_show_missing_items = True
