"""File to define Fish class."""


class Fish:
    age: int

    def __init__(self):
        self.age = 0
        return None

    def one_day(self) -> None:
        "Simulates one day for a fish where their age increases by 1"
        self.age += 1
        return None
