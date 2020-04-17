.. PINT Documentation documentation master file, created by
   sphinx-quickstart on Fri Apr 17 11:55:21 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PINT Documentation's documentation!
********************************************************

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   test-page-1

`docutils reference`_

Admonitions
============

.. NOTE:: This is a NOTE admonition!

.. IMPORTANT:: This is an IMPORTANT admonition!

.. DANGER:: This is dangerous!

.. WARNING:: This is a warning!

.. TIP:: This is a tip!

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
