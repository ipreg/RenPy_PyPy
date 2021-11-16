from __future__ import absolute_import
import importlib
import renpy
import encodings.raw_unicode_escape; encodings.raw_unicode_escape

from renpy.types import StringType
from renpy.loader import add_python_directory
py_str = StringType
add_python_directory(py_str("python-packages/lib_py"))
add_python_directory(py_str("python-packages/lib_pypy"))
add_python_directory(py_str("python-packages/py"))

renpy.store.sys.modules['py'] = importlib.import_module("py")
renpy.store.sys.modules['lib_pypy'] = importlib.import_module("lib_pypy")
renpy.store.sys.modules['lib_py'] = importlib.import_module("lib_py")
