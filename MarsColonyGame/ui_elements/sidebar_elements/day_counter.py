class DayCounter:

    def __init__(self) -> None:

        self.days_passed = 0
        self.background_color = (255, 245, 102)
    
    def increment_day(self):
        self.days_passed += 1