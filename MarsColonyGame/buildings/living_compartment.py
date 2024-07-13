from buildings.radius_building import RadiusBuilding

class LivingCompartment(RadiusBuilding):
    """
    Class representing a living compartment building in the MarsColony game.
    Inherits from RadiusBuilding.
    """

    def __init__(self, grid, x_position: int, y_position: int) -> None:
        """
        Initialize a LivingCompartment object.

        Args:
            grid (Grid): The grid where the building is placed.
            x_position (int): The x-coordinate of the building.
            y_position (int): The y-coordinate of the building.
        """
        super().__init__(grid, x_position, y_position)
        self.metal_cost: int = 2
        self.icon_path = r"MarsColonyGame\icons\living_compartment.png"
        self.info_text: str = ""
        self.needs_energy: bool = False
        self.object_name: str = "Living Compartment"

        self.provides: str = "manpower"

        self.living_space: int = 10
        self.radius: int = 3

    def update_cell_state_in_radius(self) -> None:
        """
        Update the state of cells within the building's radius.
        """
        super().update_cell_state_in_radius(self.provides)

    def show_info(self) -> None:
        """
        Display information about the building.
        """
        super().show_info()