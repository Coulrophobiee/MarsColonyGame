from buildings.radius_building import RadiusBuilding
class SolarPark(RadiusBuilding):
    
    def __init__(self, x_position, y_position) -> None:
        super().__init__(x_position, y_position)
        self.metal_cost = 2