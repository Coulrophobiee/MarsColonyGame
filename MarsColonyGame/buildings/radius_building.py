from buildings.building import Building
#from ui_elements.grid import Grid
from math import sqrt

class RadiusBuilding(Building):

    def __init__(self, grid, x_position, y_position) -> None:
        super().__init__()
        self.grid = grid
        self.radius = 5
        self.x_position = x_position
        self.y_position = y_position
        self.provides = ""
    
    def update_cell_state_in_radius(self, power_type):
        if power_type == "energy":
            for row in range(self.grid.rows):
                for col in range(self.grid.cols):
                    euclidean_distance = sqrt((self.x_position - row) ** 2 + (self.y_position - col) ** 2)
                    if euclidean_distance <= self.radius:
                        self.grid.grid[row][col].set_is_powered(True)
        elif power_type == "manpower":
            for row in range(self.grid.rows):
                for col in range(self.grid.cols):
                    euclidean_distance = sqrt((self.x_position - row) ** 2 + (self.y_position - col) ** 2)
                    if euclidean_distance <= self.radius:
                        self.grid.grid[row][col].set_is_man_powered(True)
