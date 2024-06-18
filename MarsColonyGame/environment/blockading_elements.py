from ui_elements.cell import Cell

class BlockadingElement:
    
    def __init__(self, cell) -> None:
        self.placed_on: Cell = cell
        self.icon_path = ""
        self.object_name = ""