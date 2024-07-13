from environment.blockading_elements import BlockadingElement
from ui_elements.cell import Cell

class Volcano(BlockadingElement):
    """
    A class to represent a Volcano, inheriting from BlockadingElement.
    """
    def __init__(self, cell: Cell) -> None:
        """
        Initializes a new Volcano object.

        Parameters:
        ----------
        cell : Cell
            The cell where the Volcano will be placed.
        """
        super().__init__(cell)
        self.icon_path: str = r"MarsColonyGame\icons\volcano.png"
        self.object_name: str = "Volcano"