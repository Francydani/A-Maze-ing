#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    list_players = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"]
    print()
    print(f"Initial list of players: {list_players}")
    list_capitalized = [name.capitalize() for name in list_players]

    print(f"New list with all names capitalized: {list_capitalized}")
    only_capitalized = [
        name for name in list_players if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_capitalized}")
    print()

    points = [random.randint(50, 950) for i in range(9)]
    items = {list_capitalized[i]: points[i] for i in range(len(list_players))}
    print(f"Score dict: {items}")

    average = sum(points) / len(points)
    print(f"Score average is: {round(average, 2)}")
    items_points = {
        name: score for name, score in items.items() if score > average}
    print(f"High scores: {items_points}")


if __name__ == "__main__":
    main()
