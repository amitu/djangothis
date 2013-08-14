django this
===========

This is a command line utility that django-izes the current folder. This is
primarily for prototyping.

Lets say the current folder contains a bunch of html file, this utility runs a
django server, and makes the files available through it. The html files can use
django's powerfull template inheritance.

If there is a folder named static in current folder, that content of that
folder will also become available on /static/ url.

This utility maps request to /favicon.ico to /static/favicon.ico.

Last but not the least, if there is a ajax.yaml file in current folder, this
utility will look for request the requested path in the yaml file, and if it
exists, appropriate JSON will be returned.

Take a look at an [example
folder](https://github.com/amitu/djangothis/tree/master/testsite), and compare
it with the [test
suite](https://github.com/amitu/djangothis/blob/master/djangothis/tests.py).

Installation and Usage
----------------------

To install:

.. code::

  $ pip install djangothis

To run from any folder that contains files as described above:

.. code::

  $ djangothis

