#!/usr/bin/env

def render_ascii(grid: list[list[int]]) -> None:
    """Dibuja el laberinto en la terminal usando líneas finas Unicode.

    Recorre la matriz de máscaras de bits fila por fila, mostrando las
    paredes externas e internas, la entrada, la salida y las celdas cerradas.

    Args:
        grid: Matriz bidimensional con los valores enteros de las paredes.
        entry: Coordenadas (x, y) de la entrada del laberinto.
        exit_post: Coordenadas (x, y) de la salida del laberinto.
    """
    wall = "\033[38;5;214m"
    block_sq = "\033[47m \033[0m"
    reset = "\033[0m"

    for row in grid:
        top_line = ""
        mid_line = ""
        for cell in row:
            top_line += f"{wall}┼{reset}"
            if cell & 1:
                top_line += f"{wall}───{reset}"
            else:
                top_line += "   "

            if cell & 8:
                mid_line += f"{wall}│{reset}"
            else:
                mid_line += " "

            if cell == 15:
                mid_line += f" {block_sq} "
            else:
                mid_line += "   "

        top_line += f"{wall}┼{reset}"
        if row[-1] & 2:
            mid_line += f"{wall}│{reset}"
        else:
            mid_line += " "
        print(top_line)
        print(mid_line)

    bottom_line = ""
    for cell in grid[-1]:
        bottom_line += f"{wall}┼{reset}"
        if cell & 4:
            bottom_line += f"{wall}───{reset}"
        else:
            bottom_line += "   "
    bottom_line += f"{wall}┼{reset}"
    print(bottom_line)


"""if __name__ == "__main__":
    maze = create_grid(10, 10)
    grid, visited = carve_maze(maze, (0, 0), (4, 4))
    render_ascii(grid)
    '''reset = "\033[0m"
    color = "\033[1;35;47m"
    print(f"{color}   {reset}")
    print(f"{"\033[7;35m"} Texto en negrita y subrayado de color morado {
    reset}")

    print("Hola")'''
"""
