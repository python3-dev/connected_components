import unittest
from main import Map


class TestIntegration(unittest.TestCase):
    def test_map_with_connected_buildings_0(self) -> None:
        input_map: list[list[str]]= []
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 0)

    def test_map_with_connected_buildings_0_1(self) -> None:
        input_map: list[list[str]] = [["E"]]
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 0)

    def test_map_with_connected_buildings_1_0(self) -> None:
        input_map: list[list[str]] = [["B"]]
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 1)

    def test_map_with_connected_buildings_2_1(self) -> None:
        input_map: list[list[str]] = [["B", "B"]]
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 1)

    def test_map_with_connected_buildings_2_2(self) -> None:
        input_map: list[list[str]] = [["B", "B"], ["B", "B"]]
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 1)

    def test_map_with_connected_buildings_2_2_1(self) -> None:
        input_map: list[list[str]] = [["B", "E"], ["E", "B"]]
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 2)

    def test_map_with_invalid_node(self) -> None:
        input_map: list[list[str]] = [["X", "E"], ["E", "B"]]
        map_ = Map(input_map)
        self.assertTrue(map_.invalid_map)

    def test_map_with_connected_buildings_3_3_1(self) -> None:
        input_map: list[list[str]] = [
            ["B", "B", "B"], 
            ["B", "E", "E"],
            ["B", "E", "E"],
            ]
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 1)

    def test_map_with_connected_buildings_3_2_1(self) -> None:
        input_map: list[list[str]] = [
            ["B", "B", "B"], 
            ["B", "E", "E"],
            ]
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 1)

    def test_map_with_connected_buildings_2_3_1(self) -> None:
        input_map: list[list[str]] = [
            ["B", "B"], 
            ["B", "E"],
            ["B", "E"],
            ]
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 1)

    def test_map_with_connected_buildings_2_3_1_0(self) -> None:
        input_map: list[list[str]] = [
            ["E", "E"], 
            ["E", "E"],
            ["E", "E"],
            ]
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 0)

    def test_map_with_connected_buildings_2_3_1_1(self) -> None:
        input_map: list[list[str]] = [
            ["B", "B"], 
            ["B", "B"],
            ["B", "B"],
            ]
        map_ = Map(input_map)
        self.assertEqual(map_.buildings, 1)


if __name__ == "__main__":
    unittest.main()
