#!/usr/bin/env python3

import importlib


def checker(reagent: str) -> tuple[str, str] | None:
    try:
        module = importlib.import_module(reagent)
        return module.__name__, module.__version__
    except (ImportError, AttributeError):
        return None


def main() -> None:
    print()
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")
    panda_v = checker("pandas")
    numpy_v = checker("numpy")
    if panda_v:
        print(f"[OK] {panda_v[0]} ({panda_v[1]}) - Data manipulation ready")
    else:
        print("[KO] pandas is missing!")
    if numpy_v:
        print(f"[OK] {numpy_v[0]} ({numpy_v[1]})"
              "- Numerical computation ready")
    else:
        print("[KO] numpy is missing!")
    print()

    if panda_v and numpy_v:
        print("pip vs Poetry:")
        print(" requirements.txt declares what to install; "
              "pip resolves it at install time.")
        print(" pyproject.toml declares the same constraints,"
              " and Poetry pins the resolved")
        print(" versions in poetry.lock so every install is identical.")
        print("All reagents present and accounted for.")
    else:
        print("To install missing reagents:")
        print("Using pip:")
        print("pip install -r requirements.txt")
        print()
        print("Using Poetry:")
        print("poetry install")


if __name__ == "__main__":
    main()
