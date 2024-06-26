from pygame import Vector2
from random import randint, choice
from utils.icon_manager import IconManager
from typing import Optional, Tuple

class Meteorite:
    """
    Represents a meteorite in the MarsColony game that falls from above the screen and impacts the grid.
    """

    def __init__(self, screen, grid) -> None:
        """
        Initialize a Meteorite object.

        Args:
            screen (Screen): The screen to draw the meteorite on.
            grid (Grid): The grid of cells in the game.
        """
        self.screen = screen
        self.grid = grid

        # Start at random x position
        self.x = randint(0, screen.available_grid_width)
        # Start above the screen
        self.y = -30  
        # Falling speed
        self.speed = 5 

        self.icon_path = r"MarsColonyGame\icons\meteorite.png"
        icon_manager = IconManager(grid.cell_size, self.icon_path)
        self.icon = icon_manager.get_scaled_icon()
        self.target_cell_x, self.target_cell_y = self.get_random_position()
        self.target_x, self.target_y = self.grid.get_screen_position(self.target_cell_x, self.target_cell_y)

        self.target_position = Vector2(self.target_x, self.target_y)
        self.current_position = Vector2(self.x, self.y)

    def fall(self) -> None:
        """
        Move the meteorite towards its target position. Impact the grid if it reaches the target.
        """
        if self.current_position is None:
            # Skip if already impacted
            return 
        
        if self.target_cell_x and self.target_cell_y:
            distance_to_target = self.current_position.distance_to(self.target_position)
            
            # Ensure the meteorite doesn't overshoot the target
            if distance_to_target < self.speed:
                self.current_position = self.target_position
            else:
                self.current_position = self.current_position.move_towards(self.target_position, self.speed)
                    
            if distance_to_target <= 2:
                self.impact()

    def get_random_position(self) -> Tuple[Optional[int], Optional[int]]:
        """
        Get a random position suitable for the meteorite to target.

        Returns:
            tuple: The (x, y) coordinates of the target cell in the grid.
        """
        suitable_positions = self.grid.return_cells_suitable_for_meteorite()
        if not suitable_positions:
            return None, None
        pos = choice(suitable_positions)
        print(pos)
        return pos

    def impact(self) -> None:
        """
        Handle the impact of the meteorite on the grid.
        """
        log_msg = self.grid.meteorite_impact(self.target_cell_x, self.target_cell_y)
        self.current_position = None
        self.screen.sidebar.log.add_text(log_msg)

    def draw(self) -> None:
        """
        Draw the meteorite on the screen at its current position.
        """
        if self.current_position is not None:
            self.screen.screen.blit(self.icon, (self.current_position.x, self.current_position.y))