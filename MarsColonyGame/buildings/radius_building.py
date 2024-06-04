from buildings.building import Building

class RadiusBuilding(Building):

    def __init__(self, x_position, y_position) -> None:
        super().__init__()
        self.radius = 0
        self.x_position = x_position
        self.y_position = y_position
        self.provides = ""
    
    def alter_cell_state(self):
        pass
