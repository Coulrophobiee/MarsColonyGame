from ui_elements.cell import Cell
from pygame import draw
from ui_elements.sidebar import Sidebar

class Grid:

    def __init__(self, rows, cols, cell_width, cell_height):
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(col * cell_width, row * cell_height) for col in range(cols)] for row in range(rows)]

    def draw_grid(self, screen):
        for row in self.grid:
            for cell in row:
                draw.rect(screen, cell.color, (cell.pos_x, cell.pos_y, self.cell_width, self.cell_height))
                draw.rect(screen, (0, 0, 0), (cell.pos_x, cell.pos_y, self.cell_width, self.cell_height), 1)  # Cell border

    def handle_click(self, position, sidebar:Sidebar):
        x, y = position

        # Mouse position (in pixels) divided by width of the cells equals column (x-coordinate) 
        col = x // self.cell_width
        # Mouse position (in pixels) divided by height of the cells equals row (y-coordinate) 
        row = y // self.cell_height

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
        
        
