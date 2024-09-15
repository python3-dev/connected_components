class Node:
    """Node class."""

    def __init__(
        self,
        content: str,
        row_index: int,
        column_index: int,
    ) -> None:
        self.content: str = content
        self.row_index: int = row_index
        self.column_index: int = column_index
        self.building: bool = self.content == "B"
        self.empty: bool = self.content == "E"
        if not self.building and not self.empty:
            self.invalid = True
        else:
            self.invalid = False
        self.visited: bool = False

    def visit(self) -> None:
        self.visited = True


class Map:
    """Map class."""

    def __init__(self, input_map: list[list[str]]) -> None:
        self.input_map: list[list[str]] = input_map
        self.buildings: int = 0
        self.invalid_map: bool = False
        self.row_length: int = len(input_map)
        if self.row_length > 0:
            self.column_length: int = len(input_map[0])
            self.building_nodes: dict[tuple[int, int], Node] = {}
            self.__traverse_map()
            self.__count_connected_buildings()

    def __traverse_map(self) -> None:
        for row_index, row in enumerate(self.input_map):
            for column_index, column in enumerate(row):
                node = Node(column, row_index, column_index)
                if node.building:
                    self.building_nodes[row_index, column_index] = node
                if node.invalid:
                    self.invalid_map = True

    def __count_connected_buildings(self) -> None:
        """Count the number of connected buildings."""
        for node in self.building_nodes.values():
            if node.building and not node.visited:
                self.buildings += 1
                self.__find_connected_building_nodes(node)

    def __find_connected_building_nodes(self, node: Node) -> None:
        """Find connected building nodes recursively using depth first search."""
        if node.visited:
            return
        node.visit()

        down: Node | None = self.building_nodes.get(
            (node.row_index + 1, node.column_index)
        )
        if down is not None:
            self.__find_connected_building_nodes(down)

        up: Node | None = self.building_nodes.get(
            (node.row_index - 1, node.column_index)
        )
        if up is not None:
            self.__find_connected_building_nodes(up)

        right: Node | None = self.building_nodes.get(
            (node.row_index, node.column_index + 1)
        )
        if right is not None:
            self.__find_connected_building_nodes(right)

        left: Node | None = self.building_nodes.get(
            (node.row_index, node.column_index - 1)
        )
        if left is not None:
            self.__find_connected_building_nodes(left)


if __name__ == "__main__":
    input_map: list[list[str]] = [
        ["B", "B", "B"],
        ["B", "E", "B"],
        ["E", "E", "E"],
        ["E", "E", "B"],
        ["B", "E", "B"],
    ]

    map_ = Map(input_map)
    if map_.invalid_map:
        print(-1)
    else:
        print(map_.buildings)
