#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, heigth: float, ages: int) -> None:
        self.name = name
        self.heigth = heigth
        self.ages = ages

    def show(self) -> None:
        print(f"{self.name}: {self.heigth}cm, {self.ages} days old")

    def grow(self) -> None:
        self.heigth = round(self.heigth + 0.8, 1)

    def age(self) -> None:
        self.ages += 1


def main() -> None:
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Rose", 25.0, 30)
    plant1.show()
    aux = plant1.heigth
    for i in range(1, 8):
        print("=== Day", i, "===")
        plant1.grow()
        plant1.age()
        plant1.show()
    print("Growth this week:", round(plant1.heigth - aux, 1))


if __name__ == "__main__":
    main()
