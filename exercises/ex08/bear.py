"""File to define Bear class."""


class Bear:
    """Class that sets up bear.py."""
    def __init__(self):
        """Defining self.age and self.hunger."""
        self.age = 0 
        self.hunger_score = 0 
    
    def one_day(self):
        """Aging the bear by one day and decreasing hunger_score by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish):
        """Increasing the Bear's hunger_score by num_fish."""
        self.hunger_score += num_fish