# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '《笑猫日记之绿狗山庄》阅读'
copyright = '2025, 轩宇阅读网'
author = '杨红樱'

release = '0.1.0'
version = '0.1.0'

# -- General configuration

# extensions = [
#     'sphinx.ext.duration',
#     'sphinx.ext.doctest',
#     'sphinx.ext.autodoc',
#     'sphinx.ext.autosummary',
#     'sphinx.ext.intersphinx',
# ]

# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
# }
# intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "Jason2013", # Username
    "github_repo": "smile-cat-green-dog", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/docs/source/", # Path in the checkout to the docs root
}

epub_author = "Jason2013"
epub_publisher = "https://github.com/Jason2013/"
