#!/usr/bin/env python3

import elements


def main() -> None:
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    str = elements.create_fire()
    print(f"Testing create_fire: {str}")


if __name__ == "__main__":
    main()
