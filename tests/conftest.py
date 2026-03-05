import sys
import os

# Try to import from installed package first, fall back to src for development
try:
    import yoga
except ImportError:
    # Fall back to src directory for development
    _src_dir = os.path.join(os.path.dirname(__file__), "..", "src")
    if _src_dir not in sys.path:
        sys.path.insert(0, os.path.abspath(_src_dir))
