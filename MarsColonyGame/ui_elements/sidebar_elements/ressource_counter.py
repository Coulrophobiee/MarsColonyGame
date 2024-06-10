class RessourceCounter:
    """
    Class to keep track of various resources in the MarsColony game.
    """

    def __init__(self) -> None:
        """
        Initialize a RessourceCounter object with default resource counts.
        """
        self.inhabitants_count: int = 0  # Number of inhabitants
        self.metal_count: int = 10  # Amount of metal
        self.food_count: int = 50  # Amount of food

    def get_name_of_ressource(self, ressource: str) -> str:
        """
        Get the human-readable name of a resource based on its internal representation.

        Args:
            ressource (str): The internal representation of the resource.

        Returns:
            str: The human-readable name of the resource.
        """
        if ressource == "inhabitants_count":
            return "Inhabitants"
        elif ressource == "metal_count":
            return "Metal"
        elif ressource == "food_count":
            return "Food"

    def produce_food(self) -> int:
        """
        Produce food resources.

        Returns:
            int: The amount of food produced.
        """
        return 10
    
    def produce_metal(self) -> int:
        """
        Produce metal resources.

        Returns:
            int: The amount of metal produced.
        """
        return 10