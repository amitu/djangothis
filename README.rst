django this
===========

This is a command line utility that django-izes the current folder. This is
primarily for prototyping.

Lets say the current folder contains a bunch of html file, this utility runs a
django server, and makes the files available through it. The html files can use
django's powerful template inheritance.

Config
------

djangothis supports configuring django using config.yaml file if present in
current folder. It can be used configure middleware, template context
processors etc.

Static files
------------

If there is a folder named static in current folder, that content of that
folder will also become available on /static/ url.

This utility maps request to /favicon.ico to /static/favicon.ico.

views.py and forms.py
---------------------

Further if file names views.py or forms.py exist, the utility "imports" them,
and if those files use `importd <http://pythonhosted.org/importd/>`_ style
"decorated" views or forms, they too become available (`example
<https://github.com/amitu/djangothis/blob/master/testsite/views.py>`_).

Fake Ajax
---------

Also if there is a ajax.yaml file in current folder, this utility will look for
request the requested path in the yaml file, and if it exists, appropriate JSON
will be returned.

Themes
------

djangothis supports theming. Theme can be placed in a special folder _theme.
This folder is placed at the beginning of template dirs settings, so any
template can be "overridden" by placing in it.

For the purpose of special theme specific static files, they can be placed in
side _theme folder, and will be accessible via /theme/ url. Eg if there is a
css file _theme/style.css, it can be accessed via /theme/style.css.

With these two features themes can be distributed as self contained folder.

Using djangothis as a static site generator
-------------------------------------------

.. code::

    $ wget -mk http://localhost:8000

Can be used to create a local mirror.

Using djangothis as a replacement of jekyll, pelican
----------------------------------------------------

An appropriate views.py file has to be written and placed in the current
folder, which will define views for / or /blog/, that view can read the content
of _posts for example, generate appropriate summary and links, define views for
post etc, which serve the page.

It is left for reader as an exercice. ;-)

Example site
------------

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


