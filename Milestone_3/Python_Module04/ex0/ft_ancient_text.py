#!/usr/bin/env python3

import sys
from typing import IO


def main() -> None:
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        archive: IO[str] = open(sys.argv[1], 'r')
        data = archive.read()
        archive.close()
        print("---")
        print()
        print(data)
        print()
        print("---")
        print(f"File '{sys.argv[1]}' closed.")

    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
