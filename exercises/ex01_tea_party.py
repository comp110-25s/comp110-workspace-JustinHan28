"""Program to determine how many teabags, treats, dollars are needed to throw a tea party given X number of people"""

__author__: str = "730758899"


def main_planner(guests: int) -> None:
    """Prints out the number of people, tea bags needed, treats needed, and cost"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))
    return None


def tea_bags(people: int) -> int:
    """Determines # of tea bags needed given number of people"""
    return people * 2


def treats(people: int) -> int:
    """Determines # of treats needed given number of people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Determine the cost of treats and tea_bags given number of people"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
