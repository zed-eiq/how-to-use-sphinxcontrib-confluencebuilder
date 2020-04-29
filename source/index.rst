.. PINT Documentation documentation master file, created by
   sphinx-quickstart on Fri Apr 17 11:55:21 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Getting started with sphinxcontrib-confluencebuilder
********************************************************

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   rst/index
   reusable-content
   private/docs-as-code
   notes

..  contents:: Table of contents
    :local:

Introduction
===============

This is a brief guide on how to publish rST to Confluence Server instances
using Sphinx and sphinxcontrib-confluencebuilder in your publishing
toolchain.

:reStructuredText:
  …is a markdown language (note: not *Markdown*) that
  is used in Sphinx. It is a feature rich language that,
  unfortunately, shares a predeliction for whitespace
  and magic with Python. But that *also* makes it
  a suitable markdown language for use
  with documenting Python code-bases.
:Sphinx:
  …is a Python-based static-site generator used
  to build documentation for Python code-bases.
  
  It has a powerful ``autodoc`` utility that can
  extract comments from ``.py`` files and generate
  documentation from it.

- **Repository for this set of Confluence pages**: https://github.com/zed-eiq/how-to-use-sphinxcontrib-confluencebuilder
- sphixncontrib-confluencebuilder GitHub: https://github.com/sphinx-contrib/confluencebuilder
- Forked: https://github.com/zed-eiq/confluencebuilder
- Documentation: https://sphinxcontrib-confluencebuilder.readthedocs.io/en/stable/index.html

Before using sphinxcontrib-confluencebuilder
===============================================

.. epigraph::

   HERE BE DRAGONS

Be warned! The coupling between Sphinx and Confluence is far from perfect.

Use this when you have documentation that is:

:One-way sync:
  confluencebuilder only provides one-way sync
  between your repository and confluence.
  
  This forces you to use the Sphinx documentation
  repository as your single source of truth;
  YMMV depending on where you lean re: docs-as-code.

  ..  DANGER:: **IMPORTANT** Don't lose track of where the source
      repository is located!

      sphinxcontrib-confluencebuilder only provides a one-way sync.
      If you lose the source repository, you either have to stick
      to editing the content only in Confluence, or manually
      recreate the repository by copy-pasting content.
:Does not use Scroll Versions versioning:
  Versioning with Scroll Versions does not work
  using this toolchain.

  To use sphinxcontrib-confluencebuilder and still get
  versioning, you may want to publish to a
  staging/preproduction space dedicated only for
  docs published using this toolchain,
  and then selectively copy pages over to
  the intended destinations.
:Manually adding a table of contents is wonky:
  Using the ``.. contents::`` directive to add
  a table of contents to the page adds an extra
  bullet point at the start of the list.
  
  This can probably be fixed at the theme/css
  level.

  This should already be handled by our theme.

Requirements
================

You need:

- Python 2.7 or 3.5+
- Requests 2.14.0+
- Sphinx 1.8+
- python-dotenv to pull environment variables from ``.env``
  (so we don't save our Confluence credentials to the repository).
- Confluence Server ^6.7, or `Confluence Server <7.2`_
- A user with write permissions to the target Space.

.. _Confluence Server <7.2: https://github.com/sphinx-contrib/confluencebuilder/issues/312

Getting started
================================================

You need to:

1. `Set up your project`_
2. `Configure project`_
3. `Write content!`_
4. `Publish`_

Set up your project
----------------------

In your terminal:

1.  Clone this template repository to ``my_project_directory`` and navigate to it:

    ..  code-block::

        git clone https://github.com/zed-eiq/how-to-use-sphinxcontrib-confluencebuilder my_project_directory
        cd my_project_directory

2.  (Optional) Start a Python virtual environment:

    ..  code-block::

        python -m venv env
        
        # On bash
        source env/bin/activate

        # On Windows
        env/Scripts/activate

3.  Install Python dependencies:

    ..  code-block::

        python -m pip install -r requirements.txt

You're set up! Now you need to configure your project.

Configure project
-------------------

Create a ``.env`` file at the root of ``my_project_directory``.
It should look like this:

..  code-block::

    CONFLUENCE_SERVER_URL="https://example.com/"
    USERNAME="confluence_username"
    PASSWORD="confluence_user_password"

    TARGET_SPACE="TEST"
    TARGET_PARENT_PAGE="Confluence Page Title"
    TARGET_PARENT_PAGE_ID="12345"


:CONFLUENCE_SERVER_URL:
  This is the URL at which you access your
  Confluence server.
:USERNAME:
  The user name for a Confluence user
  with write access to the ``TARGET_SPACE``.
:PASSWORD:
  The password for ``USERNAME``. 
  
  .. DANGER:: **Do not** commit **passwords** to your repository!
:TARGET_SPACE:
  Set this to the name of the Space you want to publish to.

  ..  NOTE:: I haven't tested this extensively, but looks
      like it uses the short form of the Space name e.g.
      ``TEST`` instead of ``Testing``.
:TARGET_PARENT_PAGE:
  Set this to the **title** of the parent page that you want to publish under.
  
  ``TARGET_PARENT_PAGE`` must already exist.

  ..  DANGER:: Untested! To be safe, make sure that
      the ``TARGET_PARENT_PAGE`` *only* contains content published
      from this project!

      Publishing to a page tree that already has content may
      lead to instances where pushing changes unexpectedly
      overwrites or purges content!
  
  For example, Setting this to ``"I am a parent page"``
  will publish your rST documents to:

  ..  code-block::

      TEST/
      └── "I am a parent page"
          ├── "Getting started with sphinxcontrib-confluencebuilder"
          └── "reStructuredText reference"
:TARGET_PARENT_PAGE_ID:
  Set this to the page ID of ``TARGET_PARENT_PAGE``.
  This acts as a sanity check when hitting publish,
  so that we are doubly sure that we are publishing
  to the correct ``TARGET_PARENT_PAGE``.

  To find the page ID of the ``TARGET_PARENT_PAGE``,
  navigate to the page in Confluence, and open
  **Page Information**. The page ID can be found in the
  URL of the page, which should look like this:

  ..  code-block::

      https://docs.eclecticiq.com/pages/viewinfo.action?pageId=41381991

  Take the value of ``pageId`` — which is ``41381991`` here —
  and set it as the value of ``TARGET_PARENT_PAGE_ID``.

Write content!
----------------

Write your content as ``.rst`` files in the ``source/`` folder:

- For an idea of what a rST document looks like, see :doc:`rst/rst-reference`.
- You may need a basic grasp of how Sphinx works: https://www.sphinx-doc.org/en/master/usage/quickstart.html

  - Sphinx is mostly quite resilient — output gets built
    even if the ``make``/``sphinx-build`` command shows
    several errors/warnings.

    But it's good to know how to resolve these as
    your content may not be built in the way you expect
    it to. Ping `zed <mailto:wtan@eclecticiq.com>`_ if
    you need someone to debug your rST 😬.
  - Sphinx demands that you add each page to a ``toctree`` --
    for example, at the top of the source code for this page
    is the following ``toctree`` directive:

    ..  code-block::

        .. toctree::
          :maxdepth: 2
          :caption: Contents:
          :hidden:

          rst-reference

    For more information on ``toctree``\ s, see `toctree`_

Publish
---------

To publish your project, run in the terminal:

..  code-block::

    # bash
    make confluence

    # Windows (because I haven't figured
    # out how to update the .bat file.
    sphinx-build -b confluence source build -E -a

This builds ``.conf`` files for each ``.rst`` file in your project,
and publishes them to ``TARGET_SPACE: TARGET_PARENT_PAGE`` in
your Confluence instance.

If you find that your changes are not being published,
Sphinx may not be detecting the changes in your project.
To force Sphinx to publish your project anyway:

1.  Remove the contents of the ``build`` directory:

    ..  code-block::

        make clean

        # or

        rm -rf build

        # or just delete the ``build`` directory

2.  Build the project again:

    ..  code-block::

        make confluence
        # or
        sphinx-build -b confluence source build -E -a

..  HINT:: I added an extra make command for bash that
    runs ``make clean && make confluence``, so it
    purges the build directory before building output.

Getting started from scratch
==================================

Do this if you want to set up a project from scratch
to figure out how it's done,
or if you don't trust the repo 😬:

..  code-block::

    mkdir my_project && cd my_project
    python -m venv env
    source env/bin/activate
    python -m pip install sphinx sphinx-rtd-theme sphinxcontrib-confluencebuilder python-dotenv
    python -m sphinx-quickstart
    # Follow on-screen prompts.
    # I prefer to keep source/ and build/ separate
    # as a matter of code hygiene.

    # Copy conf.py from this repository.
    # Copy _static/ directory from this repository.
    # It contains fixes for PDF and HTML output --
    # not for Confluence output but goot to have
    # a complete and working Sphinx repo.
    # Set up .env file.

toctree
=========

``toctree``\ s are how you set page order and
heirarchies in Sphinx, and are usually written
like this:

..  code-block::

    ..  toctree::

        page_one
        page_two

By default, the confluencebuilder **does not**
use the toctree to generate a page heirarchy.
Instead, it takes all pages in the Sphinx project
and publishes them on Confluence such that:

- **All pages are on the same page hierarchy level.**
  This means that even if you :ref:`nest` a page
  one or more ``toctree``\ s deep, that page is still
  published at the top level of the page hierarchy,
  under the ``TARGET_PARENT_PAGE``.
- Pages are ordered by their page titles on Confluence,
  alphabetically. This means that if the title of ``index.rst``
  is "Zebrafish — how to hunt", it is displayed after
  "How to prepare Zebrafish".

Enable page hierarchy
-----------------------

To have confluencebuilder respect the ``toctree``
when publishing to confluence, edit
``source/conf.py`` and make sure that the
following parameter is set to ``True``:

..  code-block::

    confluence_page_hierarchy = True

Once page hierarchy is enabled, confluencebuilder
publishes pages in the order they are listed
in the ``toctree`` contained in ``index.rst``.

Any pages in the project ``source/`` folder that
does not have an entry in the ``toctree`` will
still be published, but is hoisted to the same
page tree level as ``index.rst``.

.. _nest:

Nested toctrees
------------------

Not all pages have to be listed in the same
``toctree`` directive. You can group pages
by listing them in two or more ``toctree``\ s
that serve as the top-level pages for these page groups.

See how we nest the ``rst/`` group of pages in this repository,
for example:

..  code-block::

    # source/index.rst

    ..  toctree::
        :maxdepth: 2
        :caption: Contents:
        :hidden:

        rst/index

..  code-block::

    # source/rst/index.rst

    ..  toctree::

        rst-reference
        rst-style-guide

Hide the toctree
------------------

You can hide the ``toctree`` with the ``:hidden:`` option.

Do this if you need to create a ``toctree`` to define
the page hierarchy, but don't need to display
the nested pages because the
site navigation already takes care of it.
