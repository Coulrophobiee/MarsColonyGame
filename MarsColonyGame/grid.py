from cell import Cell
from pygame import draw

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

    def handle_click(self, position):
        x, y = position
        col = x // self.cell_width
        row = y // self.cell_height
        if 0 <= row < self.rows and 0 <= col <= self.cols:
            cell = self.grid[row][col]  
            cell.change_color((255, 0, 0))
