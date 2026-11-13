#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.stats: Plant.Stats = self.Stats()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self.stats.count_show()

    def ages(self) -> None:
        self.age += 1
        self.stats.count_ages()

    def grow(self) -> None:
        self.height = round(self.height + 8, 1)
        self.stats.count_grow()

    @staticmethod
    def is_older(n: int) -> bool:
        return n > 365

    @classmethod
    def unknown_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats():
        def __init__(self) -> None:
            self._age_count: int = 0
            self._grow_count: int = 0
            self._show_count: int = 0
            self._shade_count: int = 0

        def count_ages(self) -> None:
            self._age_count += 1

        def count_grow(self) -> None:
            self._grow_count += 1

        def count_show(self) -> None:
            self._show_count += 1

        def count_shade(self) -> None:
            self._shade_count += 1

        def get_age_count(self) -> int:
            return self._age_count

        def get_grow_count(self) -> int:
            return self._grow_count

        def get_show_count(self) -> int:
            return self._show_count

        def get_shade_count(self) -> int:
            return self._shade_count


class Flower(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, color: str
    ) -> None:
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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds += 42

    def grow(self) -> None:
        self.height = round(self.height + 30, 1)
        self.stats.count_grow()

    def ages(self) -> None:
        self.age += 20
        self.stats.count_ages()


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
        self.shade = True
        self.stats.count_shade()
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height}cm"
              f" long and {self.trunk_diameter}cm wide.")


def show_me(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    stats = plant.stats
    groow = stats.get_grow_count()
    agees = stats.get_age_count()
    shoow = stats.get_show_count()
    print(f"Stats: {groow} grow, {agees} age, {shoow} show")
    if plant.__class__.__name__ == "Tree":
        shadee = stats.get_shade_count()
        print(f" {shadee} shade")


def main() -> None:
    plant1 = Flower("Rose", 15.0, 10, "red")
    plant2 = Tree("Oak", 200.0, 365, 5.0)
    plant3 = Seed("Sunflower", 80.0, 45, "yellow")
    p = Plant.unknown_plant()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older(400)}")
    print()

    print("=== Flower")
    plant1.show()
    show_me(plant1)
    plant1.bloom()
    plant1.grow()
    print("[asking the rose to grow and bloom]")
    plant1.show()
    show_me(plant1)
    print()

    print("=== Tree")
    plant2.show()
    show_me(plant2)
    plant2.produce_shade()
    show_me(plant2)
    print()

    print("=== Seed")
    plant3.show()
    print("[make sunflower grow, age and bloom]")
    plant3.bloom()
    plant3.ages()
    plant3.grow()
    plant3.show()
    show_me(plant3)

    print()
    print("=== Anonymous")
    p.show()
    show_me(p)


if __name__ == "__main__":
    main()
