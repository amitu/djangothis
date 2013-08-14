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

Also if there is a ajax.yaml file in current folder, this utility will look for
request the requested path in the yaml file, and if it exists, appropriate JSON
will be returned.

Further if file names views.py or forms.py exist, the utility "imports" them,
and if those files use `importd <http://pythonhosted.org/importd/>`_ style
"decorated" views or forms, they too become available (`example
<https://github.com/amitu/djangothis/blob/master/testsite/views.py>`_).

Take a look at an `example folder
<https://github.com/amitu/djangothis/tree/master/testsite>`_, and compare it
with the `test suite
<https://github.com/amitu/djangothis/blob/master/djangothis/tests.py>`_.

Installation and Usage
----------------------

To install:

.. code::

  $ pip install djangothis

To run from any folder that contains files as described above:

.. code::

  $ djangothis
  Validating models...

  0 errors found
  Django version 1.4.1, using settings None
  Development server is running at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.


