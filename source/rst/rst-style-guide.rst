Brief style guide
************************

Follow these guidelines to make your life
working with rST text easier.

..  contents::
    :local:

Convert all tabs to spaces
================================================

Set your IDE to convert all tabs to spaces.
Trust me, this makes your life a whole lot easier.

Use 2 spaces per indent
================================================

While ``flake8`` (IIRC) demands that you use 4 spaces
per indent, it's a lot easier on the eyes
and for your sanity to use 2 spaces per indent
when working with rST, because we sometimes need
to **enforce** an even number of spaces when writing.

Enforce an even number of spaces per indent
================================================

You should manually enforce an even number of spaces
per indent. This isn't an issue for most rST syntax.
For example, list items already use an
even number of spaces per indent:

..  code-block::

    - list items
    - list items

      - sublist items
      - sublist items

However, most other elements leave you with an odd
number of spaces per indent:

..  code-block::

    .. any-directive:: leaves you with a 3-space indent
        :option_name:
    
    1. Ordered lists as well.

        - 3 space indent here.

So, to maximize sanity points and portability
between actual Python code and your rST text,
use 2 spaces per tab/indent, and enforce an even number of
spaces per indent when writing rST:

..  code-block::

    ..  any-directive:: use 4 spaces instead of 3.
        :option_name:

    1.  Use 4 spaces instead of 3.

        - 4 space indent here.

