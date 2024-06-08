from buildings.ore_mine import OreMine
from buildings.biodome import Biodome
from buildings.living_compartment import LivingCompartment
from buildings.solar_park import SolarPark
from ui_elements.sidebar_elements.ressource_counter import RessourceCounter
from ui_elements.sidebar_elements.day_counter import DayCounter
from ui_elements.grid import Grid
from ui_elements.cell import Cell

from pygame import transform, image


class Colony:

    def __init__(self, ressource_counter:RessourceCounter, day_counter:DayCounter, grid:Grid) -> None:
        self.ressource_counter = ressource_counter
        self.day_counter = day_counter
        self.inhabitants = 0
        self.grid = grid
        self.placed_generating_buildings = []
        self.placed_non_generating_buildings = []

        self.solar_panel_icon = self.load_and_scale_icons("MarsColonyGame\icons\solar-panel.png")
        self.living_compartment_icon = self.load_and_scale_icons("MarsColonyGame\icons\living_compartment.png")
        self.bio_dome_icon = self.load_and_scale_icons(r"MarsColonyGame\icons\bio-dome.png")
        self.ore_mine_icon = self.load_and_scale_icons("MarsColonyGame\icons\ore-mine.png")

    def load_and_scale_icons(self, filename):
        icon = image.load(filename)
        return transform.scale(icon, (self.grid.cell_size, self.grid.cell_size))
    
    def update_ressources(self):
        for building in self.placed_generating_buildings:
            if building.ressource_type == "food":
                self.ressource_counter.food_count += self.ressource_counter.produce_food()
            elif building.ressource_type == "metal":
                self.ressource_counter.metal_count += self.ressource_counter.produce_metal()

    def add_building(self, building_name, row, col, cell):
        if building_name == "Ore Mine":
            new_ore_mine = OreMine()
            if new_ore_mine.metal_cost < self.ressource_counter.metal_count: 
                self.placed_generating_buildings.append(new_ore_mine)
                self.ressource_counter.metal_count -= new_ore_mine.metal_cost
                cell.set_icon(self.ore_mine_icon)
                return True
        elif building_name == "Bio Dome":
            new_biodome = Biodome()
            if new_biodome.metal_cost < self.ressource_counter.metal_count:
                self.placed_generating_buildings.append(new_biodome)
                self.ressource_counter.metal_count -= new_biodome.metal_cost
                cell.set_icon(self.bio_dome_icon)
                return True
        elif building_name == "Living Compartment":
            new_living_compartment = LivingCompartment(self.grid, row, col)
            if new_living_compartment.metal_cost < self.ressource_counter.metal_count:
                self.placed_non_generating_buildings.append(new_living_compartment)
                self.ressource_counter.metal_count -= new_living_compartment.metal_cost
                cell.set_icon(self.living_compartment_icon)
                new_living_compartment.update_cell_state_in_radius()
                return True
        elif building_name == "Solar Park":
            new_solar_park = SolarPark(self.grid, row, col)
            if new_solar_park.metal_cost < self.ressource_counter.metal_count:
                self.placed_non_generating_buildings.append(new_solar_park)
                self.ressource_counter.metal_count -= new_solar_park.metal_cost
                cell.set_icon(self.solar_panel_icon)
                new_solar_park.update_cell_state_in_radius()
                return True
        return False
    

    def check_loss(self):
        if self.ressource_counter.food_count < 0:
            return False
        return True
    
    def check_win(self):
        if self.inhabitants >= 200:
            return True
        return False