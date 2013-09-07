djangothis
==========

This is a command line utility that django-izes the current folder. This is
primarily for prototyping, but can also be used for full fledged blog site.

Lets say the current folder contains a bunch of html file, this utility runs a
django server, and makes the files available through it. The html files can use
django's powerful template inheritance.

Read: `djanogthis for blogging
<http://amitu.com/2013/09/djangothis-for-blogging/>`_.

Django Templates
----------------

Any html file in the current folder is treated as a django template and is
mapped to a URL mapping their location on disk. Eg index.html will become
available on /index.html and so on.

Full power of django templates is available to these html files, so they can
use template inheritance etc. This make creating a prototype a breeze as
multiple files can inherit the look and feel of a common base.html.

Config
------

djangothis supports configuring django using config.yaml file if present in
current folder. It can be used configure middleware, template context
processors etc.

Static files
------------

If there is a folder named static in current folder, the content of that folder
will also become available on /static/ url. So static/style.css will be served
on /static/style.css.

This utility also maps request to /favicon.ico to /static/favicon.ico.

views.py and forms.py
---------------------

Further if file names views.py or forms.py exist, the utility "imports" them,
and if those files use `importd <http://pythonhosted.org/importd/>`_ style
"decorated" views or forms, they too become available (`example
<https://github.com/amitu/amitu.github.com/blob/djangothis/_theme/views.py>`_).

Fake Ajax
---------

Also if there is a ajax.yaml file in current folder, this utility will look for
request the requested path in the yaml file, and if it exists, appropriate JSON
will be returned.

Custom Tag Libraries
--------------------

A folder named templatetags in current folder can be created with __init__.py
and django template tag libraries, and djangothis will make them available to
your templates.

Custom Commands
---------------

The current folder can contain a folder cmds, which can have `django management
commands
<https://docs.djangoproject.com/en/dev/howto/custom-management-commands>`_
stored in it, along with an __init__.py.

The command can be executed by running $ djangothis commandname.

Themes
------

djangothis supports theming. Theme can be placed in a special folder _theme.
This folder is placed at the beginning of template dirs settings, so any
template can be "overridden" by placing in it.

For the purpose of special theme specific static files, they can be placed in
side _theme folder, and will be accessible via /theme/ url. Eg if there is a
css file _theme/style.css, it can be accessed via /theme/style.css.

With these two features themes can be distributed as self contained folder.

Commands, Views, Custom TemplateTags and Forms in Themes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If needed a theme can contain cmds folder, templatetags folder, views.py and
forms.py which will be included. For this feature to work the _theme folder
needs to also contain __init__.py.

Auto Reload
-----------

The debug server reloads itself when config.yaml or ajax.yaml file is updated.
Further any theme can call djangothis.watchfile(file_path) to watch a file
for modifications, so that debug server can be reloaded.

Using djangothis as a static site generator
-------------------------------------------

.. code::

    $ wget -m http://localhost:8000

Can be used to create a local mirror.

Replacing jekyll, pelican etc
-----------------------------

djangothis can be used to replace jekyll, pelican etc. For this an appropriate
views.py file has to be written and placed in the current folder or in _theme
folder, which will define views for / or /blog/, that view can read the content
of _posts for example, generate appropriate summary and links, define views for
post etc, which serve the page.

My person website, `amitu.com <http://amitu.com>`_ is powered by this, which
used to be jekyll powered. The source is available on `djangothis-jekyll
<https://github.com/amitu/djangothis-jekyll>`_.

Example site
------------

 * `amitu.com <http://amitu.com>`_, `source
   <https://github.com/amitu/amitu.github.com/tree/djangothis>`_.
 * `html5 boilerplate for djangothis
   <https://github.com/amitu/djangothis-html5-boilerplate>`_.

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


