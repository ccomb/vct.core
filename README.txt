Introduction
============

This package represents the core of VCT. It provides all basic functionalities
such as the basic objects (Issue, Observation, Action) defined with schemas, DB access,
authentification, plugin management, xmlrpc access, optional form generation, etc.

vct.core is responsible of providing a data API through xmlrpc. Users can:
- ask the server what are the available data models and generate input forms on client side
- retrieve data from the database and run queries
- feed the server with new data
- ask the server for a ready-to-use input form without handling form generation
  on the client side. This allows to dynamically display input forms with
  javascript in a page.
