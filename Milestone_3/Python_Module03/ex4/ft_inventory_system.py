#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) == 1:
        return
    print("=== Inventory System Analysis ===")
    items: dict[str, int] = {}
    views: set[str] = set()
    for arg in sys.argv[1:]:
        try:
            dic = arg.split(":")
            name = dic[0]
            if name in views:
                print(f"Redundant item '{name}' - discarding")
            else:
                views.add(name)
                count_val = int(dic[1])
                items[name] = count_val
        except ValueError:
            print(f"Quantity error for '{name}': invalid literal for int() "
                  f"with base 10: '{dic[1]}'")
        except IndexError:
            print(f"Error - invalid parameter '{arg}'")
    if items:
        print(f"Got inventory: {items}")
        lst = list(items.keys())
        print(f"Item list: {lst}")
        add = list(items.values())
        total = sum(add)
        print(f"Total quantity of the {len(add)} items: {total}")
        total_count = sum(items.values())
        for name, count in items.items():
            por = round((count / total_count) * 100, 1)
            print(f"Item {name} represents {por}%")

        def get_item_qty(k: str) -> int:
            return items[k]
        item_max = max(items, key=get_item_qty)
        print(f"Item most abundant: {item_max} "
              f"with quantity {items[item_max]}")
        item_min = min(items, key=get_item_qty)
        print(f"Item least abundant: {item_min} "
              f"with quantity {items[item_min]}")

        items.update({"magic_item": 1})
        print(f"Updated inventory: {items}")


if __name__ == "__main__":
    main()
