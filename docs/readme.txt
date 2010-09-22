VCT Core
========

Abstract
~~~~~~~~

- use from any platform and languages
- extend with plugins

Overview
~~~~~~~~
High level technical documentation
VCT Core is a package for patient care. (...)

It provides a minimal kernel, which can discuss with the outside world in two
ways: 
- an XML-RPC (or REST?) service allows the kernel to be used by 3rd party services.
- a plugin infrastructure allows the kernel to be extended with additional
  capabilities (databases, services, etc.) and to trigger external services.

You can access the VCT Core services using any language and platform, through
the use of simple XML-RPC messages. See the examples section below to discover
how to use it in different languages.


(include schema)

Examples
~~~~~~~~

Python
------

Ruby
----

PHP
---

Java
----

Plugin infrastructure
~~~~~~~~~~~~~~~~~~~~~

Different types of plugin.
To be defined more.

Data analysis plugin
--------------------

simple code examples

>>> 


Service Delegation plugin
-------------------------

A service delegation plugin allows to let some third-party service handle some
medically specialized processing.

ex: iPath

simple code examples

>>> 

Database plugin
---------------

simple code examples

>>> 


Generic Plugin tests
--------------------
We should provide generic tests for the plugin. If the third-party plugin
successfully pass the tests, it means that the plugin works.




