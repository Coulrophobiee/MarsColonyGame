from buildings.generating_building import GeneratingBuilding

class OreMine(GeneratingBuilding): 
    """
    Class representing an ore mine building in the MarsColony game.
    Inherits from GeneratingBuilding.
    """

    def __init__(self) -> None:
        """
        Initialize an OreMine object.
        """
        super().__init__("metal")
        self.icon_path = r"MarsColonyGame\icons\ore-mine.png"
        self.metal_cost: int = 2
        #self.is_powered: bool = False
        self.object_name: str = "Ore Mine" 

    def generate_ressource(self) -> int:
        """
        Generate the amount of metal resource.

        Returns:
            int: Amount of metal generated.
        """
        return 10
    