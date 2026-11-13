from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    check = dark_spell_allowed_ingredients()
    ingredient_lower = ingredients.lower()
    for item in check:
        if item in ingredient_lower:
            return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
