djangothis ChangeLog
====================

todo
----

 * enable logging for debugging theme issues

0.7 - 7-Mar-2015
----------------

 * instead of catchall view, using middleware, so it works even if there is
   another catchall view in project

0.6 - 4-Sept-2013
-----------------

 * $ djangothis gunicorn # launches gunicorn
 * raw template tag
 * .png files on / are served from static folder

0.5 - 1-Sept-2013
-----------------

 * release 0.4 was buggy
 * added arbitrary file watching support for autoreload

0.4 - 1-Sept-2013
-----------------

 * support for templatetags
 * support for management commands, in folder cmds
 * _theme folder can now also have views.py, forms.py, templatetags, cmds

0.3 - 18-Aug-2013
-----------------

 * support for config.yaml
 * support for themes
