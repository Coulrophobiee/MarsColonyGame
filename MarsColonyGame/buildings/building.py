from abc import ABC
from pygame import image
from ui_elements.cell import Cell

class Building(ABC):
    """
    Abstract base class representing a generic building in the MarsColony game.
    """

    def __init__(self) -> None:
        """
        Initialize a Building object with default attributes.
        """
        self.metal_cost: int = 0
        self.info_text: str = ""
        self.icon: image = None
        self.needs_energy: bool = True
        self.object_name: str = ""
        self.icon_path: str = ""

        self.built_on: Cell = None

    def show_info(self) -> str:
        """
        Return the information text of the building.

        Returns:
            str: Information text about the building.
        """
        return self.info_text