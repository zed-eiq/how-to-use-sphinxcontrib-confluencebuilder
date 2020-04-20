Includes examples
*************************

This page demonstrates how the ``includes`` directive
can be used to include reusable content.

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


.. _sphinx.ext.autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
