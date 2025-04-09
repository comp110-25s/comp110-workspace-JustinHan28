"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        surviving_bears: list[Bear] = []
        for selected_bear in self.bears:
            if selected_bear.age <= 5:
                surviving_bears.append(selected_bear)

        surviving_fishes: list[Fish] = []
        for selected_fish in self.fish:
            if selected_fish.age <= 3:
                surviving_fishes.append(selected_fish)
        self.bears = surviving_bears
        self.fish = surviving_fishes

        return None

    def bears_eating(self) -> None:
        for selected_bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                selected_bear.eat(3)
        return None

    def check_hunger(self) -> None:
        surviving_bears: list[Bear] = []
        for selected_bear in self.bears:
            if selected_bear.hunger_score >= 0:
                surviving_bears.append(selected_bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self) -> None:
        for _ in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self) -> None:
        for _ in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        print(f"~~~ Day {self.day}: ~~~")
        print("Fish population: " + str(len(self.fish)))
        print("Bear population: " + str(len(self.bears)))
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        for _ in range(7):
            self.one_river_day()
        return None

    def remove_fish(self, amount: int) -> None:
        for _ in range(amount):
            self.fish.pop(0)
        return None
