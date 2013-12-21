from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')
setup(
    windows = [{'script': "statpadder.py", "icon_resources": [(1, "data/samthefox.ico")]}],

    zipfile=None
)