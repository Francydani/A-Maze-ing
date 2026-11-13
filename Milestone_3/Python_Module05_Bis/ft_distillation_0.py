#!/usr/bin/env python3

from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/points.py")
    potion_1 = strength_potion()
    potion_2 = healing_potion()
    print(f"Testing strength_potion: {potion_1}")
    print(f"Testing healing_potion: {potion_2}")


if __name__ == "__main__":
    main()
