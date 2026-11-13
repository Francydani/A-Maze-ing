#!/usr/bin/env python3

import sys
from typing import IO


def main() -> None:
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
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
        try:
            print()
            print("Transform data:")
            print("---")
            print()
            line = data.splitlines()
            new_line = [f"{lines}#" for lines in line]
            new = "\n".join(new_line) + "\n"
            print(new)
            print("---")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            output = sys.stdin.readline()
            name = output.rstrip()
            if name:
                print(f"Saving data to '{name}'")
                new_archive: IO[str] = open(name, 'w')
                new_archive.write(new)
                new_archive.close()
                print(f"Data saved in file '{name}'.")
            else:
                print("Not saving data.")
        except OSError as e:
            sys.stderr.write(f"[STDERR] Error opening file '{name}': {e}\n")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")


if __name__ == "__main__":
    main()
