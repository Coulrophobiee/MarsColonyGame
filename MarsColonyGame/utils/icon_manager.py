from pygame import image, transform

class IconManager:

    def __init__(self, cell_size, icon_path) -> None:
        self.icon_size = cell_size
        self.icon_path = icon_path
    
    def get_scaled_icon(self):
        icon = image.load(self.icon_path)
        return transform.scale(icon, (self.icon_size, self.icon_size))