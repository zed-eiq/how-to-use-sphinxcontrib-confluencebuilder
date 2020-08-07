Known issue - Does not maintain page order
==============================================================

There is no way to push the page order
specified in the ``toctree`` to Confluence,
because it is not supported by the Confluence
REST API.

See CONFSERVER-40101 (opened 1 Dec 2015, last updated 18 Jul 2020):
https://jira.atlassian.com/browse/CONFSERVER-40101

See https://github.com/sphinx-contrib/confluencebuilder/issues/4
