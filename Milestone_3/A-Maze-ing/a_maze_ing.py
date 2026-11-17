import sys
from config import load_config


def main() -> None:
    try:
        if len(sys.argv) != 2:
            print("Using: python3 a_maze_ing.py <config.txt>")
            return
        data = load_config(sys.argv[1])
        print(f"Correcto\n{data}")
    except OSError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
