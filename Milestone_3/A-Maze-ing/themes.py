
RESET = "\033[0m"

BG_PINK = "\033[48;5;239m"
BG_FUCHSIA = "\033[48;5;198m"
BG_GREEN = "\033[42m"
BG_RED = "\033[41m"
BG_YELLOW = "\033[43m"
BG_WHITE = "\033[48;5;15m"
BG_CYAN = "\033[48;5;15m"
BG_GRAY = "\033[100m"
BG_FUND_PINK = "\033[48;5;225m"
BG_FUND_BLACK = "\033[48;5;16m"
FG_FUCHSIA = "\033[1;38;5;198m"
FG_CYAN = "\033[1;36m"
FG_MAGENTA = "\033[1;35m"
FG_YELLOW = "\033[1;33m"
FG_GREEN = "\033[1;32m"

THEMES: list[dict[str, str]] = [
    {
		"name": "Pinck (gray and pink)",
		"title": FG_FUCHSIA,   
		"menu": FG_CYAN,     
		"prompt": FG_GREEN,
        "wall": BG_PINK,
        "block_42": BG_FUCHSIA,
        "entry": BG_GREEN,
        "exit": BG_RED,
        "path": BG_YELLOW,
        "reset": RESET,
        "fund": BG_FUND_PINK,
    },
    {
		"name": "Darck (black and white)",
		"title": FG_FUCHSIA,   
        "menu": FG_CYAN,     
        "prompt": FG_GREEN,
        "wall": BG_WHITE,
        "block_42": BG_CYAN,
        "entry": BG_GREEN,
        "exit": BG_YELLOW,
        "path": BG_PINK,
        "reset": RESET,
        "fund": BG_FUND_BLACK,
    },
    {
		"name": "Nocturno (Gris y Amarillo)",
		"title": FG_MAGENTA,   
        "menu": FG_CYAN,     
        "prompt": FG_GREEN,
        "wall": BG_GRAY,
        "block_42": BG_YELLOW,
        "entry": BG_CYAN,
        "exit": BG_RED,
        "path": BG_GREEN,
        "reset": RESET,
        "fund": BG_FUND_BLACK,
    },
]