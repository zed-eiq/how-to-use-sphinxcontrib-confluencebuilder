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

project = 'Build pages with Sphinx and rST'
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
    #'sphinx.ext.autodoc',
    'sphinxcontrib.confluencebuilder'
]

source_suffix = '.rst'

master_doc = "index"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_includes", "private/_includes"]


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
# This tells sphinx to purge only content from the
# master_doc (page containing the top-level toctree)
# downwards instead of purging
# all content the parent page downwards
confluence_purge_from_master = True

confluence_space_name = os.environ.get("TARGET_SPACE")
# Published pages will be placed directly under
# f"{confluence_space_name}:{confluence_parent_page}"
# page must already exist
confluence_parent_page = os.environ.get("TARGET_PARENT_PAGE")

# Sanity check, so that we are SUPER sure
# that we're publishing to the correct parent page
# (to avoid catastrophic content wipes)
# Get the confluence page id by
# Going to the page, opening Page Information,
# and checking the ``pageId=xxx`` query in the
# URL that appears in the address bar.
confluence_parent_page_id_check = os.environ.get("TARGET_PARENT_PAGE_ID")

# Enables publishing page heirarchies
# If set to False, then publishes all pages
# in flat heirarchy i.e. no ordering and no nesting.
# Defaults to False; why?
# When enabled, you *must* have an index.rst
# that contains a toctree directive.
confluence_page_hierarchy=True

# confluence_publish_prefix = 'PINT'
# (or for confluence server)
confluence_server_url = os.environ.get("CONFLUENCE_SERVER_URL")
confluence_server_user = os.environ.get("USERNAME")
confluence_server_pass = os.environ.get("PASSWORD")

confluence_remove_title = True

# disable for security reasons
confluence_disable_xmlrpc = True
