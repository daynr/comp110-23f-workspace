"""File to define River class."""

__author__ = """730690615"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Setting up the River."""
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = [Fish() for _ in range(num_fish)]
        self.bears: list[Bear] = [Bear() for _ in range(num_bears)]

    def check_ages(self):
        """Checking ages."""
        new_bears = [bear for bear in self.bears if bear.age <= 5]
        new_fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = new_bears
        self.fish = new_fish

    def remove_fish(self, amount: int):
        """Removing the fish."""
        self.fish = self.fish[amount:]

    def bears_eating(self):
        """The bears eat!"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)

    def check_hunger(self):
        """Checking hunger."""
        new_bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bears = new_bears

    def repopulate_fish(self):
        """Populating the fish supply."""
        new_fish = [Fish() for _ in range(len(self.fish) // 2 * 4)]
        self.fish += new_fish

    def repopulate_bears(self):
        """Repopulating bears."""
        new_bears = [Bear() for _ in range(len(self.bears) // 2)]
        self.bears += new_bears

    def view_river(self):
        """Way to view the River."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Example of One Day."""
        self.day += 1
        for bear in self.bears:
            bear.one_day()
        for fish in self.fish:
            fish.one_day()
        self.bears_eating()
        self.check_hunger()
        self.check_ages()
        self.repopulate_fish()
        self.repopulate_bears()
        self.view_river()

    def one_river_week(self):
        """Examples of One Week."""
        for _ in range(7):
            self.one_river_day()