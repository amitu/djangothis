import os, sys, yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

__version__ = '0.9'


class FakeModuleHack:
    def __init__(self, f):
        self.__file__ = f


def watchfile(pth):
    sys.modules["djangothis::%s" % pth] = FakeModuleHack(pth)


def read_yaml_file(pth):
    try:
        return read_yaml(file(pth))
    except Exception:
        return {}


def read_yaml(pth):
    try:
        return yaml.load(pth, Loader=Loader)
    except Exception:
        return {}

from path import path
from importd import d


def dotslash(pth):
    # TODO: support directory from command line?
    return os.path.join(os.getcwd(), pth)

sys.path.append(os.getcwd())

defaults = dict(
    DEBUG=True,
    TEMPLATE_DIRS=[dotslash("_theme"), dotslash(".")],
    STATICFILES_DIRS=[dotslash("static"), dotslash("_theme")],
    INSTALLED_APPS=["djangothis"],
    TEMPLATE_CONTEXT_PROCESSORS=[
        "django.core.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "djangothis.app.context",
    ],
    SECRET_KEY=dotslash("secret.txt"),
    MIDDLEWARE_CLASSES=[
        "djangothis.app.Middleware",
    ]
)

defaults.update(read_yaml_file(dotslash("config.yaml")))

d(**defaults)

try:
    from django.template.base import add_to_builtins
except ImportError:
    from django.template.loader import add_to_builtins

from django.core.management import get_commands

try:
    import importlib
except ImportError:
    from django.utils import importlib

add_to_builtins("djangothis.templatetags.raw")


def context(request):
    return {
        "settings": d.settings
    }

try:
    import views
except ImportError:
    pass
else:
    views

try:
    import forms
except ImportError:
    pass
else:
    forms

COMMANDS = get_commands()
watchfile(dotslash("config.yaml"))
watchfile(dotslash("ajax.yaml"))

ttags = path(dotslash("templatetags"))
if ttags.exists():
    for m in ttags.walkfiles():
        if m.namebase.startswith("__"):
            continue
        if m.endswith(".py"):
            add_to_builtins("templatetags.%s" % m.namebase)

cmds = path(dotslash("cmds"))
if cmds.exists():
    for m in cmds.walkfiles():
        if m.namebase.startswith("__"):
            continue
        if m.endswith(".py"):
            try:
                cmd = importlib.import_module("cmds.%s" % m.namebase)
            except ImportError:
                pass
            else:
                sys.modules[
                    str("djangothis.management.commands.%s" % m.namebase)
                ] = cmd
                COMMANDS[m.namebase] = "djangothis"  # i <3 magic!

try:
    import _theme.views
except ImportError:
    pass
else:
    _theme.views

try:
    import _theme.forms
except ImportError:
    pass
else:
    _theme.forms

theme_ttags = path(dotslash("_theme/templatetags"))
if theme_ttags.exists():
    for m in theme_ttags.walkfiles():
        if m.namebase.startswith("__"):
            continue
        if m.endswith(".py"):
            add_to_builtins("_theme.templatetags.%s" % m.namebase)

theme_cmds = path(dotslash("_theme/cmds"))
if theme_cmds.exists():
    for m in theme_cmds.walkfiles():
        if m.namebase.startswith("__"):
            continue
        if m.endswith(".py"):
            try:
                cmd = importlib.import_module("_theme.cmds.%s" % m.namebase)
            except ImportError:
                pass
            else:
                sys.modules[
                    str("djangothis.management.commands.%s" % m.namebase)
                ] = cmd
                COMMANDS[m.namebase] = "djangothis"  # i <3 magic!

from django.contrib.staticfiles.views import serve
from fhurl import JSONResponse


class Middleware(object):
    def process_response(self, request, response):
        if response is d.Http404:
            return response

        path = request.path[1:]

        if path == "favicon.ico" or path.endswith(".png"):
            return serve(request, path)

        if path.startswith("theme"):
            return serve(request, request.path[len("/theme/"):])

        if path == "" or path.endswith("/"):
            path = path + "index.html"

        if os.path.exists(dotslash(path)) and os.path.isfile(dotslash(path)):
            return d.render_to_response(
                path, {}, d.RequestContext(request)
            )

        ajax = read_yaml_file(dotslash("ajax.yaml"))

        if ajax:
            if request.GET:
                path = request.path + "?" + request.META["QUERY_STRING"]
                # TODO: make it immune to order of GET params
                if path in ajax:
                    return JSONResponse(ajax[path])
            if request.path in ajax:
                return JSONResponse(ajax[request.path])

        if not request.path.endswith("/"):
            return d.HttpResponseRedirect(request.path + "/")

        return response


if __name__ == "__main__":
    d.main()
