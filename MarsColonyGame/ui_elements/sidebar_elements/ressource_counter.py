class RessourceCounter:
    """
    Class to keep track of various resources in the MarsColony game.
    """

    def __init__(self) -> None:
        """
        Initialize a RessourceCounter object with default resource counts.
        """
        self.inhabitants_count: int = 0
        self.metal_count: int = 10
        self.food_count: int = 50

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