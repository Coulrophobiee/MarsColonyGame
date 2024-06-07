class RessourceCounter:
    def __init__(self) -> None:
        self.inhabitants_count = 0
        self.metal_count = 5
        self.food_count = 0

    def get_name_of_ressource(self, ressource):
        if ressource == "inhabitants_count":
            return "Inhabitants"
        elif ressource == "metal_count":
            return "Metal"
        elif ressource == "food_count":
            return "Food"

    def produce_food(self):
        return 10
    
    def produce_metal(self):
        return 10

    def update_inhabitants_count():
        pass