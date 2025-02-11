# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'coding-test'
copyright = '2025, hyojin-joo'
author = 'hyojin-joo'
release = 'v0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys

from recommonmark.parser import CommonMarkParser
sys.path.insert(0, os.path.abspath('.'))

source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

extensions = ['recommonmark']

templates_path = ['_templates']
exclude_patterns = []

language = 'ko'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_favicon = "favicon.ico"
