from ui_elements.cell import Cell
from ui_elements.sidebar import Sidebar
from colony import Colony
from pygame import Surface

class Grid:
    """
    Represents the grid of cells in the MarsColony game.
    """

    def __init__(self, available_width: int, available_height: int, min_cell_size: int = 20) -> None:
        """
        Initialize a Grid object.

        Args:
            available_width (int): The available width for the grid.
            available_height (int): The available height for the grid.
            min_cell_size (int, optional): The minimum size of each cell. Defaults to 20.
        """
        cell_size = min(available_width // min_cell_size, available_height // min_cell_size)
        
        # Calculate actual rows and columns based on cell size
        self.cols: int = available_width // cell_size
        self.rows: int = available_height // cell_size
        self.cell_size: int = cell_size
        
        # Create the grid of cells
        self.grid: list[list[Cell]] = [[Cell(col * cell_size, row * cell_size, cell_size) for col in range(self.cols)] for row in range(self.rows)]
        

    def draw_grid(self, screen: Surface) -> None:
        """
        Draw the grid of cells on the screen.

        Args:
            screen (Surface): The surface to draw the grid on.
        """
        for row in self.grid:
            for cell in row:
                cell.draw(screen)

    def handle_click(self, position: tuple[int, int], sidebar: Sidebar, colony: Colony) -> None:
        """
        Handle mouse click on the grid.

        Args:
            position (tuple[int, int]): The position of the mouse click.
            sidebar (Sidebar): The sidebar object.
            colony (Colony): The colony object.
        """
        x, y = position

        # Mouse position (in pixels) divided by width of the cells equals column (x-coordinate) 
        col: int = x // self.cell_size
        # Mouse position (in pixels) divided by height of the cells equals row (y-coordinate) 
        row: int = y // self.cell_size

        # Cell is the corresponding cell object at the grid position (initialized in the grid)
        cell: Cell = self.grid[row][col]

        if sidebar.selected_building and not cell.is_occupied:
            # Add building to colony if enough resources
            if not colony.add_building(sidebar.selected_building, row, col, cell):
                print(f"Not enough resources for {sidebar.selected_building}")
            else:
                # Occupy cell 
                cell.is_occupied = True

            # Unselect building after placement
            sidebar.selected_building = None

        elif sidebar.selected_building and cell.is_occupied:
            sidebar.log.add_text("Cell is occupied,\n you can't build here!")
        elif sidebar.selected_building is None:
            sidebar.log.add_text(cell.show_info())
    
    def return_unoccupied_cells(self)->list:
        unoccupied_positions = []
        for row in range(self.rows):
            for col in range(self.cols):
                cell: Cell = self.grid[row][col]
                if not cell.is_occupied:
                    unoccupied_positions.append((row, col))
        return unoccupied_positions