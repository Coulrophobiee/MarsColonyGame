from buildings.building import Building

class GeneratingBuilding(Building):

    def __init__(self, ressource_type) -> None:
        super().__init__()
        self.ressource_type = ressource_type
        self.needs_manpower =  True


    def generate_ressource(self):
        pass
    
