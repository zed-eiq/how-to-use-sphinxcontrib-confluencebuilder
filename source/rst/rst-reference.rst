reStructuredText reference
******************************

Official documentation for reStructuredText (rST): `docutils reference`_

Below are examples of how rST is rendered in Confluence.

..  contents::
    :depth: 2

Text styles
==================

- **Bold**
- *Italics*

Links
======

There's no way to use `Confluence's link magic`_
when working with ``sphinxcontrib-confluencebuilder``.

You'll need to use direct and full links to content on
docs.eclecticiq.com. For example, to link to the `Integrations`_
page, you need to point to ``https://docs.eclecticiq.com/integrations``.

..  list-table:: Link syntax
    :width: 100%
    :widths: auto
    :header-rows: 1
    :stub-columns: 1
    :align: left

    * - Link type
      - Example rST
    * - Inline links
      - 
        ..  code-block::

            `Inline link <https://example.com/#anchor>`_
        
        **Result**: `Inline link <https://example.com/#anchor>`_
    * - References (recommended)
      -
        ..  code-block::

            `Link by reference`_

            ...

            .. _Link by reference: https://example.com/#anchor

        **Result**: `Link by reference`_
    * - Link to implicit header anchors
      - Link to headers by enclosing the header *verbatim*
        in backticks (``\```). Note that this doesn't work with
        *all* headers — especially headers with excessive punctuation
        (that shouldn't be in headers in the first place).

        ..  code-block::
            
            `Admonitions`_

        **Result**: `Admonitions`_


Admonitions
============

.. NOTE:: This is a NOTE admonition!

   Notice that the ``NOTE`` admonition is
   actually rendered as an ``Info`` Confluence macro.

.. ATTENTION:: This is an ATTENTION admonition!
   
   The ``ATTENTION`` and ``CAUTION`` admonitions
   are rendered as the ``Note`` Confluence macro.

   .. CAUTION:: This is a CAUTION admonition!

.. IMPORTANT:: This is an IMPORTANT admonition!
   
   The ``IMPORTANT``, ``DANGER``,
   and ``WARNING`` admonitions are rendered the
   same way.

   .. DANGER:: This is dangerous!

   .. WARNING:: This is a warning!

   .. ERROR:: This is an ERROR admonition!

.. TIP:: This is a tip!

   You can also write ``TIP`` as ``HINT``
   to get the ``Tip`` Confluence macro.

   .. HINT:: This is a hint!

Tables
=========

.. csv-table::
   :widths: 15 10 30
   :width: 100%
   :header-rows: 1

   this, is, a
   csv, table,


You can also `import a CSV file`_ as a table with the ``csv-table`` directive:

.. csv-table:: Imported CSV table
   :width: 100%
   :header-rows: 1
   :file: ../_includes/test.csv

.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :width: 100%
   :header-rows: 1
   :stub-columns: 1
   :align: left

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!


.. _docutils reference: https://docutils.sourceforge.io/docs/ref/rst/directives.html

.. _Link by reference: https://example.com/#anchor

.. _Confluence's link magic: https://docs.eclecticiq.com/pages/viewpage.action?pageId=41377063
.. _Integrations: https://docs.eclecticiq.com/integrations
.. _Import a CSV file: https://github.com/zed-eiq/how-to-use-sphinxcontrib-confluencebuilder/tree/master/source/includes/test.csv
