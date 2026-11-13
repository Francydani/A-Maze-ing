#!/usr/bin/env python3

import random

achievements = ["Crafting Genius", "Strategist", "World Savior",
                "Speed Runner", "Survivor", "Master Explorer",
                "Treasure Hunter", "Unstoppable", "First Steps",
                "Collector Supreme", "Untouchable", "Sharp Mind",
                "Boss Slayer"]


def gen_player_achievements() -> set[str]:
    achievement_lst = random.sample(achievements, 6)
    return set(achievement_lst)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    player_1 = "Alice"
    player_2 = "Bob"
    player_3 = "Charlie"
    player_4 = "Dylan"

    player_a = gen_player_achievements()
    player_b = gen_player_achievements()
    player_c = gen_player_achievements()
    player_d = gen_player_achievements()
    print(f"Player {player_1}: {player_a}")
    print(f"Player {player_2}: {player_b}")
    print(f"Player {player_3}: {player_c}")
    print(f"Player {player_4}: {player_d}")
    print()

    distinct = player_a.union(player_b, player_c, player_d)
    print(f"All distinct achievements: {distinct}")
    print()

    com = player_a.intersection(player_b, player_c, player_d)
    print(f"Common achievements: {com}")
    print()
    only_a = player_a.difference(player_b, player_c, player_d)
    only_b = player_b.difference(player_a, player_c, player_d)
    only_c = player_c.difference(player_b, player_a, player_d)
    only_d = player_d.difference(player_b, player_c, player_a)
    print(f"Only {player_1} has: {only_a}")
    print(f"Only {player_2} has: {only_b}")
    print(f"Only {player_3} has: {only_c}")
    print(f"Only {player_4} has: {only_d}")
    print()

    achi = set(achievements)
    missing_a = achi.difference(player_a)
    missing_b = achi.difference(player_b)
    missing_c = achi.difference(player_c)
    missing_d = achi.difference(player_d)
    print(f"{player_1} is missing: {missing_a}")
    print(f"{player_2} is missing: {missing_b}")
    print(f"{player_3} is missing: {missing_c}")
    print(f"{player_4} is missing: {missing_d}")


if __name__ == "__main__":
    main()
