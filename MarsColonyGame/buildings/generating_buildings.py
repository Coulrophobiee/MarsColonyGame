from buildings.building import Building

class GeneratingBuildings(Building):

    def __init__(self) -> None:
        super().__init__()
        self.ressource_type = None
        self.needs_manpower =  True


    def generate_ressource(self, ressource_type, ressource_count):
        ressource_count += 1 
    
