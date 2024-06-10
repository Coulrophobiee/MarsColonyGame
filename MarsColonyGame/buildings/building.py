from abc import ABC, abstractmethod

class Building(ABC):
    def __init__(self) -> None:
        self.metal_cost = 0
        self.info_text = ""
        self.icon_path = ""
        self.needs_energy = True
        self.building_name = ""

    def show_info(self):
        return self.info_text
    
