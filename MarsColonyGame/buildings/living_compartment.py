from buildings.radius_building import RadiusBuilding

class LivingCompartment(RadiusBuilding):
    def __init__(self, x_position, y_position) -> None:
        super().__init__(x_position, y_position)
        self.building_cost = 10 #?
        self.icon_path = ""
        self.info_text = ""
        self.needs_energy = False

        self.provides = "manpower"

        self.living_space = 10
        self.radius = 3
        
    def alter_cell_state(self):
        return super().alter_cell_state()

    def show_info(self):
        return super().show_info()