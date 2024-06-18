from buildings.ore_mine import OreMine
from buildings.biodome import Biodome
from buildings.living_compartment import LivingCompartment
from buildings.solar_park import SolarPark
from ui_elements.sidebar_elements.ressource_counter import RessourceCounter
from ui_elements.sidebar_elements.day_counter import DayCounter
from utils.icon_manager import IconManager
from pygame import transform, image


class Colony:

    def __init__(self, ressource_counter: RessourceCounter, day_counter: DayCounter, grid) -> None:
        """
        Initialize the colony with the given resource counter, day counter, and grid.

        Args:
            ressource_counter (RessourceCounter): The resource counter for the colony.
            day_counter (DayCounter): The day counter for the colony.
            grid: The grid for the colony.
        """
        self.ressource_counter = ressource_counter
        self.day_counter = day_counter
        self.grid = grid
        self.placed_generating_buildings = []
        self.placed_non_generating_buildings = []

    def spawn_starting_buildings(self) -> None:
        """
        Spawn the starting buildings for the colony.
        """
        self.add_building("Ore Mine", 10, 10, self.grid.grid[10][10])
        self.grid.grid[10][10].is_occupied = True
        self.add_building("Living Compartment", 11, 11, self.grid.grid[11][11])
        self.grid.grid[11][11].is_occupied = True
        self.add_building("Solar Park", 12, 12, self.grid.grid[12][12])
        self.grid.grid[12][12].is_occupied = True

    def load_and_scale_icons(self, filename: str):
        """
        Load and scale the icons for the colony.

        Args:
            filename (str): The filename of the icon.

        Returns:
            pygame.Surface: The scaled icon.
        """
        icon = image.load(filename)
        return transform.scale(icon, (self.grid.cell_size, self.grid.cell_size))

    def generate_ressources(self) -> None:
        """
        Generate resources for the colony.
        """
        for building in self.placed_generating_buildings:
            if building.built_on.is_powered and building.built_on.is_manpowered:
                if building.ressource_type == "food":
                    self.ressource_counter.food_count += building.generate_ressource()
                elif building.ressource_type == "metal":
                    self.ressource_counter.metal_count += building.generate_ressource()

    def consume_food(self) -> None:
        """
        Consume food for the colony.
        """
        self.ressource_counter.food_count -= self.ressource_counter.inhabitants_count

    def add_building(self, building_name: str, row: int, col: int, cell) -> bool:
        """
        Add a building to the colony.

        Args:
            building_name (str): The name of the building.
            row (int): The row index.
            col (int): The column index.
            cell: The cell to add the building to.

        Returns:
            bool: True if the building is successfully added, False otherwise.
        """
        # Define a mapping of building names to their corresponding classes and icons
        building_info = {
            "Ore Mine": (OreMine, self.placed_generating_buildings),
            "Bio Dome": (Biodome, self.placed_generating_buildings),
            "Living Compartment": (LivingCompartment,  self.placed_non_generating_buildings),
            "Solar Park": (SolarPark, self.placed_non_generating_buildings),
        }

        if building_name in building_info:
            building_class,  building_list = building_info[building_name]

            # Create a new building instance
            if building_name in ["Living Compartment", "Solar Park"]:
                new_building = building_class(self.grid, row, col)
            else:
                new_building = building_class()

            # Check if enough resources are available
            if new_building.metal_cost <= self.ressource_counter.metal_count:
                # Deduct resource cost
                self.ressource_counter.metal_count -= new_building.metal_cost
                
                # Add building to the appropriate list
                building_list.append(new_building)
                
                # Set icon and occupy the cell
                new_building.built_on = cell
                icon_manager = IconManager(cell.size, new_building.icon_path)
                new_building.icon = icon_manager.get_scaled_icon()
                cell.set_icon(new_building.icon)
                cell.occupied_with = new_building

                # Update building's powered state based on the cell's state
                # if cell.is_powered:
                #     new_building.is_powered = True
                # if cell.is_manpowered:
                #     new_building.is_man_powered = True

                # Special handling for Living Compartment and Solar Park
                if building_name == "Living Compartment":
                    self.ressource_counter.inhabitants_count += new_building.living_space
                if building_name in ["Living Compartment", "Solar Park"]:
                    new_building.update_cell_state_in_radius()

                return True
        return False

    def has_failed(self) -> bool:
        """
        Check if the colony has failed.

        Returns:
            bool: True if the colony has failed, False otherwise.
        """
        if self.ressource_counter.food_count < 0:
            return True
        return False
    
    def has_succeded(self) -> bool:
        """
        Check if the colony has succeeded.

        Returns:
            bool: True if the colony has succeeded, False otherwise.
        """
        if self.ressource_counter.inhabitants_count >= 200:
            return True
        return False