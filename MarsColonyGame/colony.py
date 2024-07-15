from buildings.ore_mine import OreMine
from buildings.biodome import Biodome
from buildings.living_compartment import LivingCompartment
from buildings.solar_park import SolarPark
from ui_elements.sidebar_elements.ressource_counter import RessourceCounter
from ui_elements.sidebar_elements.day_counter import DayCounter
from utils.icon_manager import IconManager
from random import choice, sample

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
        potential_positions = self.grid.return_unoccupied_cells()
        if not potential_positions:
            print("No unoccupied cells available.")
            return

        # Step 1: select random position
        initial_position = choice(potential_positions)
        initial_x, initial_y = initial_position

        # Step 2: change position to avoid edge spawns
        grid_width = self.grid.rows
        grid_height = self.grid.cols

        def adjust_position(x, y):
            if x < 4:
                x = 4
            elif x > grid_width - 5:
                x = grid_width - 5
            if y < 4:
                y = 4
            elif y > grid_height - 5:
                y = grid_height - 5
            return x, y

        initial_x, initial_y = adjust_position(initial_x, initial_y)

        # Step 3: Generate neighboring positions
        neighbors = [
            (initial_x + dx, initial_y + dy)
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            if (dx != 0 or dy != 0) and 0 <= initial_x + dx < grid_width and 0 <= initial_y + dy < grid_height
        ]

        # Ensure that neighboring positions are unoccupied
        neighbors = [(x, y) for (x, y) in neighbors if not self.grid.grid[x][y].is_occupied]

        # Step 4: Randomly select two more positions from neighbors
        additional_positions = sample(neighbors, 2)
        positions = [(initial_x, initial_y)] + additional_positions

        buildings = ["Ore Mine", "Living Compartment", "Solar Park"]
        for building, (x, y) in zip(buildings, positions):
            self.add_building(building, x, y, self.grid.grid[x][y])
            self.grid.grid[x][y].is_occupied = True

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