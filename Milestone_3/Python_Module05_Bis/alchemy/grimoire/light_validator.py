def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    check = light_spell_allowed_ingredients()
    ingredient_lower = ingredients.lower()
    for item in check:
        if item in ingredient_lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
