#!/usr/bin/env

from themes import THEMES


def render_ascii(
        grid: list[list[int]],
        entry: tuple[int, int],
        exit_post: tuple[int, int],
        theme: dict[str, str]) -> None:
    """Dibuja el laberinto en la terminal usando caracteres ASCII.

    Recorre la matriz de máscaras de bits fila por fila, mostrando las
    paredes externas e internas junto con la entrada y la salida.

    Args:
        grid: Matriz bidimensional con los valores enteros de las paredes.
        entry: Coordenadas (x, y) de la entrada del laberinto.
        exit_post: Coordenadas (x, y) de la salida del laberinto.
    """
    color = theme["wall"]
    entry_sq = theme["entry"]
    exit_sq = theme["exit"]
    reset = theme["reset"]
    block_color = theme["block_42"]
    fund_color =theme["fund"]
    for y, row in enumerate(grid):
        top_line = ""
        mid_line = ""
        for x, cell in enumerate(row):
            is_42 = (cell == 15)
            top_42 = (y > 0 and grid[y - 1][x] == 15)
            left_42 = (x > 0 and grid[y][x - 1] == 15)
            diag_42 = (x > 0 and y > 0 and grid[y - 1][x - 1] == 15)
            c_corner = (
                block_color
                if (is_42 or top_42 or left_42 or diag_42)
                else color)
            c_north = block_color if (is_42 or top_42) else color
            c_west = block_color if (is_42 or left_42) else color

            top_line += c_corner + "  " + reset
            if cell & 1:
                top_line += c_north + "  " + reset
            else:
                top_line +=  fund_color + "  " + reset
            if cell & 8:
                mid_line += c_west + "  " + reset
            else:
                mid_line += fund_color + "  " + reset

            if is_42:
                mid_line += "\033[48;5;207m" + "  " + reset
            elif (x, y) == entry:
                mid_line += entry_sq + "  " + reset
            elif (x, y) == exit_post:
                mid_line += exit_sq + "  " + reset
            else:
                mid_line += fund_color + "  " + reset
        top_line += color + "  " + reset
        if row[-1] & 2:
            mid_line += color + "  " + reset
        else:
            mid_line += fund_color + "  " + reset
        print(top_line)
        print(mid_line)
    bottom_line = ""
    for cell in grid[-1]:
        bottom_line += color + "  " + reset
        if cell & 4:
            bottom_line += color + "  " + reset
        else:
            bottom_line += fund_color + "  " + reset
    bottom_line += color + "  " + reset
    print(bottom_line)



