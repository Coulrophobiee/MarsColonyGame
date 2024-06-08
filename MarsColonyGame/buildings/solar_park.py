from buildings.radius_building import RadiusBuilding
class SolarPark(RadiusBuilding):
    
    def __init__(self, grid, x_position, y_position) -> None:
        super().__init__(grid, x_position, y_position)
        self.metal_cost = 2
        self.radius = 5
        self.provides = "energy"

    def update_cell_state_in_radius(self):
        return super().update_cell_state_in_radius(self.provides)