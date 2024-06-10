from buildings.generating_building import GeneratingBuilding

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
        self.metal_cost: int = 2  # Cost in metal to build the Bio Dome
        self.building_name: str = "Bio Dome"  # Name of the building

    def generate_ressource(self) -> int:
        """
        Generate the amount of food produced by the Bio Dome.

        Returns:
            int: Amount of food generated.
        """
        return 10
        
    

