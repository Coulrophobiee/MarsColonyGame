from ui_elements.cell import Cell

class BlockadingElement:
    """
    Parent class for environmental objects on the Mars
    """
    
    def __init__(self, cell: Cell) -> None:
        """
        Initializes a new BlockadingElement.

        Parameters:
        ----------
        cell : Cell
            The cell where the blockading element will be placed.
        """
        self.placed_on: Cell = cell
        self.icon_path: str = ""
        self.object_name: str = ""