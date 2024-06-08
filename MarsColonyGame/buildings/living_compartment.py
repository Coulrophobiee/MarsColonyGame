from buildings.radius_building import RadiusBuilding

class LivingCompartment(RadiusBuilding):
    def __init__(self, grid, x_position, y_position) -> None:
        super().__init__(grid, x_position, y_position)
        self.metal_cost = 2 #?
        self.icon_path = ""
        self.info_text = ""
        self.needs_energy = False

        self.provides = "manpower"

        self.living_space = 10
        self.radius = 3

    def update_cell_state_in_radius(self):
        return super().update_cell_state_in_radius(self.provides)
    def show_info(self):
        return super().show_info()