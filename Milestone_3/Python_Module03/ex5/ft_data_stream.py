#!/usr/bin/env python3

import random
from typing import Generator


def gen_event(
    players: list[str], actions: list[str]
) -> Generator[tuple[str, str], None, None]:
    while True:
        player_ramdom = random.choice(players)
        action_random = random.choice(actions)
        yield (player_ramdom, action_random)


def consume_event(
    list_gener: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while list_gener:
        clean_random = random.choice(list_gener)
        list_gener.remove(clean_random)
        yield clean_random


def main() -> None:
    list_players = ["Bob", "Alice", "Dylan", "Charlie", "Dani"]
    list_actions = ["run", "eat", "sleep", "grab", "move",
                    "climb", "swim", "release"]

    print("=== Game Data Stream Processor ===")
    gener = gen_event(list_players, list_actions)
    for i in range(1000):
        res = next(gener)
        print(f"Event {i}: Player {res[0]} did action {res[1]}")
    list_gener = [next(gener) for i in range(10)]
    print(f"Built list of 10 events: {list_gener}")
    for event in consume_event(list_gener):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_gener}")


if __name__ == "__main__":
    main()
