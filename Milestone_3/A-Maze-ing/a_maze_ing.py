import sys
from config import load_config
from maze_generator import MazeGenerator
from render import render_ascii
from output import save_maze


def main() -> None:
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 a_maze_ing.py <config.txt>")
            return
        data = load_config(sys.argv[1])
        print(f"Correcto\n{data}")

        generator = MazeGenerator(data)
        generator.maze_maker()
        if generator.grid is not None:
            render_ascii(generator.grid)
            save_maze(
                data["OUTPUT_FILE"], generator.grid,
                data["ENTRY"], data["EXIT"],
                "NSEO")

    except OSError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
