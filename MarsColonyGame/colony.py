from buildings.ore_mine import OreMine
from buildings.biodome import Biodome
from ui_elements.sidebar_elements.ressource_counter import RessourceCounter
from ui_elements.sidebar_elements.day_counter import DayCounter


class Colony:

<<<<<<< HEAD
    def __init__(self, ressource_counter:RessourceCounter, day_counter:DayCounter) -> None:
        self.ressource_counter = ressource_counter
        self.day_counter = day_counter
=======
    def __init__(self) -> None:
        self.day = 0
        self.metal = 0
        self.food = 0
>>>>>>> 92f4e867721282332f8d434e34198423f50b49a7
        self.inhabitants = 0
        self.placed_generating_buildings = []

    def update_ressources(self):
<<<<<<< HEAD
        for building in self.generating_buildings:
            if building.ressource_type == "food":
                self.ressource_counter.food_count += self.ressource_counter.produce_food()
            elif building.ressource_type == "metal":
                self.ressource_counter.metal_count += self.ressource_counter.produce_metal()
=======
        for generating_building in self.placed_generating_buildings:
            if generating_building.ressource_type == "food":
                self.food += generating_building.generate_ressources()
            elif generating_building.ressource_type == "metal":
                self.metal += generating_building.generate_ressources()
>>>>>>> 92f4e867721282332f8d434e34198423f50b49a7

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