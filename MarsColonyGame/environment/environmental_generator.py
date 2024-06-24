from environment.mars_rock import MarsRock
from environment.volcano import Volcano
from ui_elements.grid import Grid
from ui_elements.cell import Cell
from utils.icon_manager import IconManager
from random import choice

class EnvironmentalGenerator:

    def __init__(self) -> None:
        self.amounts_to_generate = {Volcano: 70, MarsRock: 70}

    def generate(self, grid: Grid):
        potential_positions = grid.return_unoccupied_cells()
        
        for object_class, amount in self.amounts_to_generate.items():
            for _ in range(amount):
                position = choice(potential_positions)
                potential_positions.remove(position)

                cell: Cell = grid.grid[position[0]][position[1]]
                cell.is_occupied = True
                environmental_object = object_class(cell)
                cell.occupied_with = environmental_object
                icon_manager = IconManager(grid.cell_size, environmental_object.icon_path)
                cell.set_icon(icon_manager.get_scaled_icon())