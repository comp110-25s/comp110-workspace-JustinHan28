"""File to define Bear class."""


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Simulates one day in river simulation where a bear's age increases by one and hunger score goes down by one"""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Increases a hunger score but number of fishes eaten"""
        self.hunger_score += num_fish
        return None
