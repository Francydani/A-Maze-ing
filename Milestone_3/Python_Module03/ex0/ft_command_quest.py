#!/usr/bin/env python3

import sys

print("=== Command Quest ===")
if len(sys.argv) == 1:
    print(f"Program name: {sys.argv[0]}")
    print("No arguments provided!")
    print("Total arguments:", len(sys.argv))

elif len(sys.argv) > 1:
    print("Program name:", sys.argv[0])
    print("Arguments received:", (len(sys.argv) - 1))
    i = 1
    while i < len(sys.argv):
        print(f"Arguments {i}: {sys.argv[i]}")
        i += 1
    print("Total arguments:", len(sys.argv))
