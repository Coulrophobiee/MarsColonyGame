from buildings.generating_building import GeneratingBuilding

class OreMine(GeneratingBuilding):
    def __init__(self) -> None:
        super().__init__("metal")
        self.metal_cost = 2
        self.is_powered = False

    def generate_ressource(self):
        return 10
    