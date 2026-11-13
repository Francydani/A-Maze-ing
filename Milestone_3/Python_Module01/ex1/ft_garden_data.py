#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, heigth: int, age: int) -> None:
        self.name = name
        self.heigth = heigth
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.heigth}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 30, 120)
    plant3 = Plant("Cactus", 10, 12)
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()
