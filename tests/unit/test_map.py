import unittest
from main import Map

class TestMap(unittest.TestCase):
    def test_init(self) -> None:
        input_map: list[list[str]] = [["B", "E"], ["E", "B"]]
        map_ = Map(input_map)
        self.assertEqual(map_.input_map, input_map)
        self.assertEqual(map_.buildings, 2)
        self.assertFalse(map_.invalid_map)

    def test_traverse_map(self) -> None:
        input_map: list[list[str]] = [["B", "E"], ["E", "B"]]
        map_ = Map(input_map)
        self.assertEqual(len(map_.building_nodes), 2)

    def test_count_connected_buildings(self) -> None:
        input_map: list[list[str]] = [["B", "B"], ["B", "B"]]
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 1)

    def test_invalid_map(self) -> None:
        input_map: list[list[str]] = [["X", "E"], ["E", "B"]]
        map_ = Map(input_map)
        self.assertTrue(map_.invalid_map)