from buildings.building import Building
from math import sqrt
from ui_elements.cell import Cell

class RadiusBuilding(Building):
    """
    A class representing a building that can influence cells within a certain radius.
    """

    def __init__(self, grid, x_position: int, y_position: int) -> None:
        """
        Initializes a RadiusBuilding instance.

        Args:
            grid (Grid): The grid on which the building is placed.
            x_position (int): The x-coordinate position of the building on the grid.
            y_position (int): The y-coordinate position of the building on the grid.
        """
        super().__init__()
        self.grid = grid
        self.radius: int = None
        self.x_position: int = x_position
        self.y_position: int = y_position
        self.provides: str = ""

    def update_cell_state_in_radius(self, power_type: str) -> None:
        """
        Updates the state of cells within the building's radius based on the provided power type.

        Args:
            power_type (str): The type of power to provide ("energy" or "manpower").

        Raises:
            ValueError: If an unsupported power type is provided.
        """
        if power_type not in {"energy", "manpower"}:
            raise ValueError("Unsupported power type. Use 'energy' or 'manpower'.")

        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                euclidean_distance = sqrt((self.x_position - row) ** 2 + (self.y_position - col) ** 2)
                if euclidean_distance <= self.radius:
                    cell: Cell = self.grid.grid[row][col]
                    if power_type == "energy":
                        cell.set_is_powered(True)
                    elif power_type == "manpower":
                        cell.set_is_man_powered(True)