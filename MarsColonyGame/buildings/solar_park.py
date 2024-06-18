from buildings.radius_building import RadiusBuilding
from pygame import image

class SolarPark(RadiusBuilding):
    """
    Class representing a solar park building in the MarsColony game.
    Inherits from RadiusBuilding.
    """

    def __init__(self, grid, x_position: int, y_position: int) -> None:
        """
        Initialize a SolarPark object.

        Args:
            grid (Grid): The grid in which the building is placed.
            x_position (int): The x-coordinate of the building's position.
            y_position (int): The y-coordinate of the building's position.
        """
        super().__init__(grid, x_position, y_position)
        self.icon_path: str = r"MarsColonyGame\icons\solar-panel.png"
        self.metal_cost: int = 2
        self.radius: int = 5
        self.provides: str = "energy"
        self.building_name: str = "Solar Park"

    def update_cell_state_in_radius(self) -> None:
        """
        Update the state of cells within the building's radius.
        Calls the parent method to perform the update based on the resource provided.
        """
        super().update_cell_state_in_radius(self.provides)