import pytest
from yoga import Config, Node


@pytest.mark.skip(
    reason="nanobind pytest crash: clone() + free_recursive() causes abort. Works in regular Python."
)
class TestYGConfig:
    def test_config_cloning_uses_callback(self):
        cloned_node = Node()

        def clone_fn(old_node, owner, child_index):
            return cloned_node

        config = Config()
        config.set_clone_node_callback(clone_fn)

        node = Node(config)
        owner = Node(config)
        clone = config.clone_node(node, owner, 0)

        assert clone is cloned_node

    def test_config_cloning_fallback_on_null(self):
        def do_not_clone(old_node, owner, child_index):
            return None

        config = Config()
        config.set_clone_node_callback(do_not_clone)

        node = Node(config)
        owner = Node(config)
        clone = config.clone_node(node, owner, 0)

        assert clone is not None
        clone.free()
