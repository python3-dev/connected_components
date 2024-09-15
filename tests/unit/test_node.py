import unittest
from main import Node

class TestNode(unittest.TestCase):
    def test_init_building(self) -> None:
        node = Node("B", 0, 0)
        self.assertEqual(node.content, "B")
        self.assertEqual(node.row_index, 0)
        self.assertEqual(node.column_index, 0)
        self.assertTrue(node.building)
        self.assertFalse(node.empty)
        self.assertFalse(node.visited)

    def test_init_empty(self) -> None:
        node = Node("E", 0, 0)
        self.assertEqual(node.content, "E")
        self.assertEqual(node.row_index, 0)
        self.assertEqual(node.column_index, 0)
        self.assertTrue(node.empty)
        self.assertFalse(node.building)
        self.assertFalse(node.visited)

    def test_init_invalid(self) -> None:
        node = Node("X", 0, 0)
        self.assertTrue(node.invalid)

    def test_visit(self) -> None:
        node = Node("B", 0, 0)
        node.visit()
        self.assertTrue(node.visited)