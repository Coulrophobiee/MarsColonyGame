from environment.blockading_elements import BlockadingElement

class Volcano(BlockadingElement):

    def __init__(self, cell) -> None:
        super().__init__(cell)
        self.icon_path = r"MarsColonyGame\icons\volcano.png"
        self.object_name = "Volcano"