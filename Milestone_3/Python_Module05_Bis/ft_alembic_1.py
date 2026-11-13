#!/usr/bin/env python3


import alchemy


def main() -> None:
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    str = alchemy.create_air()
    print(f"Testing create_air: {str}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth:")
    print(f"{alchemy.create_earth()}")


if __name__ == "__main__":
    main()
