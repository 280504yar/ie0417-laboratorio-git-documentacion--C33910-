# Configuration file for the Sphinx documentation builder.
#
# Documentación generada para el proyecto NumPy como parte del laboratorio
# de Git y documentación de software.

# -- Project information -----------------------------------------------------

project = 'NumPy - Documentación Sphinx'
copyright = '2026, Yara'
author = 'Yara'
release = '2.x'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'numpydoc',
]

autosummary_generate = True

autoclass_content = 'both'

templates_path = ['_templates']

exclude_patterns = []

language = 'es'


# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'

html_static_path = ['_static']

html_title = 'NumPy - Documentación Sphinx'


# -- Autodoc configuration ---------------------------------------------------

autodoc_member_order = 'bysource'

autodoc_typehints = 'description'


# -- Numpydoc configuration --------------------------------------------------

numpydoc_show_class_members = True

numpydoc_class_members_toctree = False