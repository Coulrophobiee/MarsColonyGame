from buildings.ore_mine import OreMine
from buildings.biodome import Biodome
from buildings.living_compartment import LivingCompartment
from buildings.solar_park import SolarPark
from ui_elements.sidebar_elements.ressource_counter import RessourceCounter
from ui_elements.sidebar_elements.day_counter import DayCounter


class Colony:

    def __init__(self, ressource_counter:RessourceCounter, day_counter:DayCounter) -> None:
        self.ressource_counter = ressource_counter
        self.day_counter = day_counter
        self.inhabitants = 0
        self.placed_generating_buildings = []
        self.placed_non_generating_buildings = []

    def update_ressources(self):
        for building in self.placed_generating_buildings:
            if building.ressource_type == "food":
                self.ressource_counter.food_count += self.ressource_counter.produce_food()
            elif building.ressource_type == "metal":
                self.ressource_counter.metal_count += self.ressource_counter.produce_metal()

    def add_building(self, building_name, x_position, y_position):
        if building_name == "Ore Mine":
            new_ore_mine = OreMine()
            if new_ore_mine.metal_cost < self.ressource_counter.metal_count: 
                self.placed_generating_buildings.append(new_ore_mine)
                self.ressource_counter.metal_count -= new_ore_mine.metal_cost
                return True
        elif building_name == "Bio Dome":
            new_biodome = Biodome()
            if new_biodome.metal_cost < self.ressource_counter.metal_count:
                self.placed_generating_buildings.append(new_biodome)
                self.ressource_counter.metal_count -= new_biodome.metal_cost
                return True
        elif building_name == "Living Compartment":
            new_living_compartment = LivingCompartment(x_position, y_position)
            if new_living_compartment.metal_cost < self.ressource_counter.metal_count:
                self.placed_non_generating_buildings.append(new_living_compartment)
                self.ressource_counter.metal_count -= new_living_compartment.metal_cost
                return True
        elif building_name == "Solar Park":
            new_solar_park = SolarPark(x_position, y_position)
            if new_solar_park.metal_cost < self.ressource_counter.metal_count:
                self.placed_non_generating_buildings.append(new_solar_park)
                self.ressource_counter.metal_count -= new_solar_park.metal_cost
                return True
        return False
    

    def check_loss(self):
        if self.food < 0:
            return False
        return True
    
    def check_win(self):
        if self.inhabitants >= 200:
            return True
        return False