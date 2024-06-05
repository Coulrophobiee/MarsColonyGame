from buildings.generating_building import GeneratingBuilding

class Biodome(GeneratingBuilding):
    def __init__(self) -> None:
        super().__init__("food")

    def generate_ressource(self):
        return 10
        
    

