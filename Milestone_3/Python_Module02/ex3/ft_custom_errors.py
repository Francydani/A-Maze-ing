#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(name: str, water_level: int, temp: int) -> None:
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")
    elif temp < 12:
        raise PlantError(f"The {name} plant is wilting!")


def test_custom_exceptions(name: str, water_level: int, temp: int) -> None:
    try:
        check_plant(name, water_level, temp)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    test_custom_exceptions("Tomato", 12, 0)
    print()
    print("Testing WaterError...")
    test_custom_exceptions("Water", 1, 25)
    print()
    print("Testing catching all garden errors...")
    try:
        check_plant("Tomato", 12, 0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_plant("Water", 1, 25)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
