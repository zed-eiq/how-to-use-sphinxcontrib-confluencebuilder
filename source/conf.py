# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.append(os.path.abspath('.'))
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path('..')/'.env')

# -- Project information -----------------------------------------------------

project = 'PINT Documentation'
copyright = '2020, EclecticIQ B.V.'
author = 'EclecticIQ B.V.'

# The full version, including alpha/beta/rc tags
release = '2.7.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinxcontrib.confluencebuilder'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    #'canonical_url': '',
    #'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # 'vcs_pageview_mode': 'raw1',
    # 'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 2,
    'includehidden': True,
    'titles_only': False,
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/css/fixes.css',  # overrides for wide tables in RTD theme
        ],
    }

# LaTeX things

# inside conf.py
latex_engine = 'xelatex'
latex_elements = {
#     'fontpkg': r'''
# \setmainfont{DejaVu Serif}
# \setsansfont{DejaVu Sans}
# \setmonofont{DejaVu Sans Mono}
# ''',
    'preamble': r'''
\usepackage{enumitem}\setlistdepth{99}
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'

# sphinxcontrib.confluencebuilder options
confluence_publish = True

"""
..  WARNING: DO NOT ENABLE unless you know what you're doing.
    
    Set to ``False`` by default.

    When ``confluence_purge`` is enabled,
    it cleans out *everything* under ``confluence_parent_page``
    and publishes fresh copies of the contents of this
    repository to it.
"""
confluence_purge = False # True

confluence_space_name = 'DEV'
# Published pages will be placed directly under
# f"{confluence_space_name}:{confluence_parent_page}"
# page must already exist
confluence_parent_page = 'Build pages with Sphinx and rST'
# confluence_publish_prefix = 'PINT'
# (or for confluence server)
confluence_server_url = 'https://docs.eclecticiq.com/'
confluence_server_user = os.environ.get("USERNAME")
confluence_server_pass = os.environ.get("PASSWORD")

confluence_disable_xmlrpc = True
