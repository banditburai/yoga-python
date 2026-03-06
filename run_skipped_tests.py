#!/usr/bin/env python3
"""
Run yoga-python tests that are skipped in pytest due to nanobind pytest crash.

These tests work in regular Python but crash in pytest due to a known
nanobind issue with clone() + free_recursive().

Run this script to verify these tests pass:
    python run_skipped_tests.py
"""

import sys
import os

# Ensure yoga is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tests"))


def run_tests():
    """Run all tests that are skipped in pytest."""
    passed = 0
    failed = 0

    print("Running yoga-python tests that are skipped in pytest...")
    print("=" * 60)

    # Test 1: test_clone_node.py
    print("\n1. Running test_clone_node.py...")
    try:
        from test_clone_node import TestCloneNode

        test = TestCloneNode()
        test.test_absolute_node_cloned_with_static_parent()
        test.test_absolute_node_cloned_with_static_ancestors()
        print("   PASSED")
        passed += 2
    except Exception as e:
        print(f"   FAILED: {e}")
        failed += 2

    # Test 2: test_persistence.py
    print("\n2. Running test_persistence.py...")
    try:
        from test_persistence import TestPersistence

        test = TestPersistence()
        test.test_cloning_shared_root()
        print("   PASSED")
        passed += 1
    except Exception as e:
        print(f"   FAILED: {e}")
        failed += 1

    # Test 3: test_persistent_node_cloning.py
    print("\n3. Running test_persistent_node_cloning.py...")
    try:
        from test_persistent_node_cloning import TestPersistentNodeCloning

        test = TestPersistentNodeCloning()
        test.test_changing_sibling_height_does_not_clone_neighbors()
        print("   PASSED")
        passed += 1
    except Exception as e:
        print(f"   FAILED: {e}")
        failed += 1

    # Test 4: test_events.py
    print("\n4. Running test_events.py...")
    try:
        from test_events import TestEvents

        test = TestEvents()
        test.test_new_node_has_event()
        test.test_free_node_event()
        print("   PASSED")
        passed += 2
    except Exception as e:
        print(f"   FAILED: {e}")
        failed += 2

    # Test 5: test_config.py
    print("\n5. Running test_config.py...")
    try:
        from test_config import TestYGConfig

        test = TestYGConfig()
        test.test_config_cloning_uses_callback()
        print("   PASSED")
        passed += 1
    except Exception as e:
        print(f"   FAILED: {e}")
        failed += 1

    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")

    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
