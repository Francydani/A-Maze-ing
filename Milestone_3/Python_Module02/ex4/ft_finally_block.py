#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    name = plant_name.capitalize()
    if plant_name == name:
        print(f"Watering {name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")

    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")

    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
