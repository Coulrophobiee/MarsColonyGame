class DayCounter:
    """
    Class to keep track of the number of days passed in the MarsColony game.
    """

    def __init__(self) -> None:
        """
        Initialize a DayCounter object with default attributes.
        """
        self.days_passed: int = 0
        self.background_color: tuple[int, int, int] = (255, 245, 102)

    def increment_day(self) -> None:
        """
        Increment the day counter by one.
        """
        self.days_passed += 1