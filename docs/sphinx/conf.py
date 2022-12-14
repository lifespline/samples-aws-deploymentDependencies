# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
# task runner docs
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'lifespline-samples-aws-deploymentDependencies'
copyright = '2022, lifespline'
author = 'lifespline'
release = '1.0.0-beta'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # display docs build time
    'sphinx.ext.duration',

    # process docstrings in src
    'sphinx.ext.autodoc',

    # test code snippets
    'sphinx.ext.doctest',

    # typedoc
    'sphinx_js'
]

# typedoc
js_language = 'typescript'
js_source_path = '../../lib/*.ts'
jsdoc_config_path = '../../typedoc.json'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
