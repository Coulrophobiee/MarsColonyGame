from pygame import image, transform, Surface

class IconManager:
    """
    Manages icons for display in the MarsColony game.
    """

    def __init__(self, cell_size: int, icon_path: str) -> None:
        """
        Initialize an IconManager object.

        Args:
            cell_size (int): The size of the cell where the icon will be displayed.
            icon_path (str): The file path to the icon image.
        """
        self.icon_size: int = cell_size
        self.icon_path: str = icon_path
    
    def get_scaled_icon(self) -> Surface:
        """
        Load and scale the icon to fit the specified cell size.

        Returns:
            Surface: The scaled icon surface.
        """
        icon: Surface = image.load(self.icon_path)
        return transform.scale(icon, (self.icon_size, self.icon_size))