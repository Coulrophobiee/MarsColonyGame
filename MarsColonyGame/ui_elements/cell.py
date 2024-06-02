class Cell:
    
    def __init__(self, pos_x, pos_y, size) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size
        # Default Color is white 
        self.color = (139, 69, 19)
        self.is_occupied = False
        self.is_powered = False
        self.is_man_powered = False
        self.occupied_with = None

    def change_color(self, color):
        self.color = color
    
    def show_info(self):
        print(f"Is occupied: {self.is_occupied}, is occupied with: {self.occupied_with}, is powered: {self.is_powered}, is manpowered: {self.is_man_powered}")