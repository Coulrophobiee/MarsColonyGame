from ui_elements.cell import Cell
from ui_elements.sidebar import Sidebar
#from colony import Colony

class Grid:

    def __init__(self, available_width, available_height, min_cell_size=20):
        cell_size = min(available_width // min_cell_size, available_height // min_cell_size)
        
        # Calculate actual rows and columns based on cell size
        self.cols = available_width // cell_size
        self.rows = available_height // cell_size
        self.cell_size = cell_size
        
        # Create the grid of cells
        self.grid = [[Cell(col * cell_size, row * cell_size, cell_size) for col in range(self.cols)] for row in range(self.rows)]
        

    def draw_grid(self, screen):
        for row in self.grid:
            for cell in row:
                cell.draw(screen)

    def handle_click(self, position, sidebar:Sidebar, colony):
        x, y = position

        # Mouse position (in pixels) divided by width of the cells equals column (x-coordinate) 
        col = x // self.cell_size
        # Mouse position (in pixels) divided by height of the cells equals row (y-coordinate) 
        row = y // self.cell_size

        # Cell is the corresponding cell object at the grid position (initialized in the grid)
        cell = self.grid[row][col]
        if sidebar.selected_building and not cell.is_occupied:

            # Add building to colony if enough ressources
            if not colony.add_building(sidebar.selected_building, row, col, cell):
                print(f"Not enough ressources for {sidebar.selected_building}")
            else:
                # Occupy cell 
                cell.is_occupied = True

            # Unselect building after placement
            sidebar.selected_building = None

        elif sidebar.selected_building and cell.is_occupied:
            print("Cell is already occupied, you cannot build here!")
        elif sidebar.selected_building == None:
            cell.show_info()
    