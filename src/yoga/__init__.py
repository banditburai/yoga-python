"""
Yoga Python bindings - Facebook Yoga layout engine

This package provides Python bindings for the Facebook Yoga layout engine.
Uses compiled C++ PyBind11 extension.
"""

import os
import sys
import importlib.util

# Get the directory where this __init__.py is located
_package_dir = os.path.dirname(__file__)

# Check for compiled extension (yoga.cpython-*.so)
_compiled_path = None
for f in os.listdir(_package_dir):
    if f.startswith("yoga.") and (f.endswith(".so") or f.endswith(".dylib")):
        _compiled_path = os.path.join(_package_dir, f)
        break

if _compiled_path:
    # Load the compiled extension directly with the correct module name
    spec = importlib.util.spec_from_file_location("yoga", _compiled_path)
    if spec and spec.loader:
        _compiled = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_compiled)

        # Copy all public attributes from compiled module
        for attr in dir(_compiled):
            if not attr.startswith("_"):
                try:
                    globals()[attr] = getattr(_compiled, attr)
                except Exception:
                    pass

        __all__ = [attr for attr in dir(_compiled) if not attr.startswith("_")]
else:
    raise ImportError("Yoga compiled extension not found!")
