from setuptools import setup
import os, re, codecs

def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts)).read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

descr = "Serve static files and django templates in current folder."

setup(
    name = "djangothis",
    description = descr,
    long_description=read("README.rst"),

    version = find_version("djangothis/app.py"),
    author = 'Amit Upadhyay',
    author_email = "upadhyay@gmail.com",

    url = 'http://amitu.com/djangothis/',
    license = 'BSD',

    install_requires = ["importd>=0.2.3", "PyYAML"],
    packages = ["djangothis"],

    zip_safe = False,
    entry_points=dict(console_scripts=['djangothis=djangothis.app:d.main']),
)
