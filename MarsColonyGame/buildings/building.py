from abc import ABC
from pygame import image, transform
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
        self.building_name: str = ""
        self.icon_path: str = ""

        self.built_on: Cell = None

    def show_info(self) -> str:
        """
        Return the information text of the building.

        Returns:
            str: Information text about the building.
        """
        return self.info_text
    
    def load_and_scale_icon(self)->image:
        """
        Load and scale the icons for the colony.

        Args:
            filename (str): The filename of the icon.

        Returns:
            pygame.image: The scaled icon.
        """
        icon = image.load(self.icon_path)
        return transform.scale(icon, (self.built_on.size, self.built_on.size))
        
