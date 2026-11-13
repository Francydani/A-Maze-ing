#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed: bool = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name}, is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self.bloomed = True
        print("[asking the rose to bloom]")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade: bool = False

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.shede = True
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height}cm"
              f" long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value: int = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def ages(self) -> None:
        self.age += 1

    def grow(self) -> None:
        self.height = round(self.height + 2.1, 1)
        self.nutritional_value += 1


def main() -> None:
    plant1 = Flower("Rose", 15.0, 10, "red")
    plant2 = Tree("Oak", 200.0, 365, 5.0)
    plant3 = Vegetable("Tomato", 5.0, 10, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    plant1.show()
    plant1.bloom()
    plant1.show()
    print()

    print("=== Tree")
    plant2.show()
    plant2.produce_shade()
    print()

    print("=== Vegetable")
    plant3.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        plant3.ages()
        plant3.grow()
    plant3.show()


if __name__ == "__main__":
    main()
