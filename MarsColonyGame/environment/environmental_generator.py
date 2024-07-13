from environment.mars_rock import MarsRock
from environment.volcano import Volcano
from ui_elements.grid import Grid
from ui_elements.cell import Cell
from utils.icon_manager import IconManager
from random import choice

class EnvironmentalGenerator:
    """
    A class to generate environmental objects on a grid.

    Attributes:
    ----------
    amounts_to_generate : dict
        A dictionary mapping classes of environmental objects to the amounts to generate.
    """

    def __init__(self) -> None:
        """
        Initializes the EnvironmentalGenerator with default amounts to generate for each environmental object.
        """
        self.amounts_to_generate = {Volcano: 60, MarsRock: 60}

    def generate(self, grid: Grid) -> None:
        """
        Generates the specified amounts of environmental objects on the grid.

        Parameters:
        ----------
        grid : Grid
            The grid on which to generate the environmental objects.
        """
        # Get a list of all unoccupied cells in the grid
        potential_positions = grid.return_unoccupied_cells()
        
        # Iterate over each object class and the amount to generate
        for object_class, amount in self.amounts_to_generate.items():
            for _ in range(amount):
                # Randomly select a position from the list of potential positions
                position = choice(potential_positions)
                # Remove the selected position from the list to avoid re-selection
                potential_positions.remove(position)

                # Get the cell at the selected position in the grid
                cell: Cell = grid.grid[position[0]][position[1]]
                # Mark the cell as occupied
                cell.is_occupied = True
                # Create an instance of the environmental object and place it in the cell
                environmental_object = object_class(cell)
                cell.occupied_with = environmental_object

                # Set the icon for the cell using the scaled icon from the IconManager
                icon_manager = IconManager(grid.cell_size, environmental_object.icon_path)
                cell.set_icon(icon_manager.get_scaled_icon())