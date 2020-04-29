Reusable content
*************************

This page demonstrates how the ``includes`` directive
can be used to include reusable content.

..  contents::
    :local:

Text substitutions
====================

Official documentation for `substitutions`_/variables/reusable snippets.

To define a substitution:

..  code-block::

    .. |<snippet-name>| replace:: <what to replace it with>

    For example:

    .. |rST| replace:: reStructuredText 🎉

Result:

.. |rST| replace:: reStructuredText 🎉

|rST|

Limitations
-------------

You cannot use substitutions in:

- inline code snippets like ``this``.
- ``code-block`` directives.
- as the label for any directive.

Including code snippets
==============================

You can include code snippets in your content:

..  include:: _includes/example.py
    :number-lines:
    :code:

Note that while you can import raw python files with
the ``include`` directive, and it *looks* like
it's parsing the ``.py`` file and generating documentation
for it — it is not:

..  admonition:: Example

    ..  include:: _includes/example.py

To document ``.py`` source files, use
`sphinx.ext.autodoc`_ instead.

.. _substitutions: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#substitutions
.. _sphinx.ext.autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
