from buildings.building import Building
from abc import ABC, abstractmethod

class GeneratingBuilding(Building, ABC):

    def __init__(self, ressource_type) -> None:
        super().__init__()
        self.ressource_type = ressource_type
        self.needs_manpower =  True
        self.is_powered = False
        self.is_man_powered = False

    @abstractmethod
    def generate_ressource(self):
        pass
    
