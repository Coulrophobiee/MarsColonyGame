class RessourceCounter:
    def __init__(self) -> None:
        self.inhabitants_count = 0
        self.metal_count = 0
        self.food_count = 0

    def get_name_of_ressource(self, ressource):
        if ressource == "inhabitants_count":
            return "Inhabitants"
        elif ressource == "metal_count":
            return "Metal"
        elif ressource == "food_count":
            return "Food"

<<<<<<< HEAD
    def produce_food(self):
        return 10
    
    def produce_metal(self):
        return 10
=======
    def update_generated_ressources(self):
        pass
>>>>>>> 92f4e867721282332f8d434e34198423f50b49a7

    def update_inhabitants_count():
        pass