from buildings.ore_mine import OreMine
from buildings.biodome import Biodome

class Colony:

    def __init__(self) -> None:
        self.day = 0
        self.metal = 0
        self.food = 0
        self.inhabitants = 0
        self.placed_generating_buildings = []

    def update_ressources(self):
        for generating_building in self.placed_generating_buildings:
            if generating_building.ressource_type == "food":
                self.food += generating_building.generate_ressources()
            elif generating_building.ressource_type == "metal":
                self.metal += generating_building.generate_ressources()

    def add_building(self, building_name):
        if building_name == "Ore Mine":
            new_ore_mine = OreMine()
            self.placed_generating_buildings.append(new_ore_mine)
        elif building_name == "Bio Dome":
            new_biodome = Biodome()
            self.placed_generating_buildings.append(new_biodome)
    
    def check_loss(self):
        if self.food < 0:
            return False
        return True
    
    def check_win(self):
        if self.inhabitants >= 200:
            return True
        return False