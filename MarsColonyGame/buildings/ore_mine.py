from buildings.generating_building import GeneratingBuilding

class OreMine(GeneratingBuilding):
    def __init__(self) -> None:
        super().__init__("metal")

    def generate_ressource(self):
        return 10
    