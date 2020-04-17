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
   :header-rows: 1

   this, is, a
   csv, table,

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
   :header-rows: 1

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
