from environment.blockading_elements import BlockadingElement
from ui_elements.cell import Cell


class MarsRock(BlockadingElement):
    """
    A class to represent a Mars Rock, inheriting from BlockadingElement.
    """
    def __init__(self, cell:Cell) -> None:
        """
        Initializes a new MarsRock object.

        Parameters:
        ----------
        cell : Cell
            The cell where the Mars Rock will be placed.
        """
        super().__init__(cell)
        self.icon_path: str = r"MarsColonyGame\icons\mars-rock.png"
        self.object_name: str = "Rock"