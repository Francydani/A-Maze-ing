def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    tex = seed_type.capitalize()
    if unit == "packets":
        print(tex, "seeds:", quantity, "packets aviable")
    elif unit == "grams":
        print(tex, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(tex, "seeds:", "covers", quantity, "square meters")
    else:
        print("Unknown unit type")
