"""Punto de entrada principal y menú interactivo de A-Maze-ing."""

import sys
from typing import Any
from config import load_config
from maze_generator import MazeGenerator
from render import render_ascii
from output import save_maze
from themes import THEMES


def create_and_save(data: dict[str, Any], theme: dict[str, str]) -> MazeGenerator:
    """Genera un nuevo laberinto, lo guarda en disco y lo dibuja."""
    generator = MazeGenerator(data)
    generator.maze_maker()
    if generator.grid is not None:
        render_ascii(generator.grid, data["ENTRY"], data["EXIT"], theme)
        save_maze(
            data["OUTPUT_FILE"],
            generator.grid,
            data["ENTRY"],
            data["EXIT"],
            "NSEO",
        )
    return generator


def print_menu(theme: dict[str, str]) -> str:
    """Muestra el menú interactivo aplicando los colores del tema activo."""
    reset = theme["reset"]
    title = theme["title"]
    menu = theme["menu"]
    prompt = theme["prompt"]

    print(f"\n{title}=== A-Maze-ing ==={reset}")
    print(f"{menu}1. Re-generate a new maze")
    print("2. Show / Hide the shortest path")
    print("3. Rotate the wall colours")
    print(f"4. Quit{reset}")
    return input(f"{prompt}Choice? (1-4): {reset}").strip()



def main() -> None:
    """Carga la configuración, genera el laberinto y gestiona el menú."""
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 a_maze_ing.py <config.txt>")
            return
        data = load_config(sys.argv[1])
        theme_idx = 0
        show_path = False
        generator = create_and_save(data, THEMES[theme_idx])
        if generator.grid is None:
            return

        while True:
            choice = print_menu(THEMES[theme_idx])
            if choice == "1":
                generator = create_and_save(data, THEMES[theme_idx])
            elif choice == "2":
                show_path = not show_path
                print(f"Show path: {show_path} (pendiente de conectar BFS)")
            elif choice == "3":
                theme_idx = (theme_idx + 1) % len(THEMES)
                render_ascii(
                    generator.grid,
                    data["ENTRY"],
                    data["EXIT"],
                    THEMES[theme_idx],
                )
            elif choice == "4":
                break
            else:
                print("Invalid option. Please enter a number from 1 to 4.")

    except (OSError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
