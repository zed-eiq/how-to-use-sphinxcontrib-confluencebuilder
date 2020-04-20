Notes
*********

make latexpdf is broken
===========================

Building pdf output with ``make latexpdf`` is broken.

PDF output produces a document that does not follow
the page hierarchy defined by ``toctrees`` -- and
appears to render them in reverse order e.g.
``index`` is placed last.
