from buildings.generating_building import GeneratingBuilding
from pygame import image

class Biodome(GeneratingBuilding):
    """
    Class representing a Bio Dome building in the MarsColony game.
    Bio Dome generates food as its resource.
    """

    def __init__(self) -> None:
        """
        Initialize a Biodome object with default attributes.
        """
        super().__init__("food")
        self.icon_path:str = r"MarsColonyGame\icons\bio-dome.png"
        self.metal_cost: int = 2
        self.building_name: str = "Bio Dome"

    def generate_ressource(self) -> int:
        """
        Generate the amount of food produced by the Bio Dome.

        Returns:
            int: Amount of food generated.
        """
        return 12
        
    

