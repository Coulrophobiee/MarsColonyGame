from ui_elements.cell import Cell
from pygame import draw
from ui_elements.sidebar import Sidebar

class Grid:

    def __init__(self, available_width, available_height):
        cell_size = min(available_width // 20, available_height // 20)
        
        # Calculate actual rows and columns based on cell size
        self.cols = available_width // cell_size
        self.rows = available_height // cell_size
        self.cell_size = cell_size

        # Calculate the grid dimensions
        grid_width = self.cols * cell_size
        grid_height = self.rows * cell_size

        # Adjust the sidebar height to match the grid height
        self.sidebar_height = grid_height
        
        # Create the grid of cells
        self.grid = [[Cell(col * cell_size, row * cell_size, cell_size) for col in range(self.cols)] for row in range(self.rows)]
        # self.cell_size = cell_size
        # self.rows = rows
        # self.cols = cols
        # self.grid = [[Cell(col * cell_size, row * cell_size, cell_size) for col in range(cols)] for row in range(rows)]

    def draw_grid(self, screen):
        for row in self.grid:
            for cell in row:
                # Cell 
                draw.rect(screen, cell.color, (cell.pos_x, cell.pos_y, self.cell_size, self.cell_size))
                # Cell border
                draw.rect(screen, (0, 0, 0), (cell.pos_x, cell.pos_y, self.cell_size, self.cell_size), 1) 

    def handle_click(self, position, sidebar:Sidebar):
        x, y = position

        # Mouse position (in pixels) divided by width of the cells equals column (x-coordinate) 
        col = x // self.cell_size
        # Mouse position (in pixels) divided by height of the cells equals row (y-coordinate) 
        row = y // self.cell_size

        # if 0 <= row < self.rows and 0 <= col < self.cols:

        # Cell is the corresponding cell object at the grid position (initialized in the grid)
        cell = self.grid[row][col]
        if sidebar.selected_building and not cell.is_occupied:
            # TODO: instead of changing color - place selected building

            # Change color to green to represent the building
            cell.change_color((0, 255, 0))
            cell.is_occupied = True
            # TODO: Show the building built via an icon/image, 

            # Unselect building after placement
            sidebar.selected_building = None
        elif sidebar.selected_building and cell.is_occupied:
            print("Cell is already occupied, you cannot build here!")
        elif sidebar.selected_building == None:
            cell.show_info()
        
        
