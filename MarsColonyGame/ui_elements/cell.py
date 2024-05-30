class Cell:
    powered: bool
    man_powered: bool
    
    def __init__(self, pos_x, pos_y) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        # Default Color is white 
        self.color = (255, 255, 255)
        self.is_occupied = False


    def change_color(self, color):
        self.color = color