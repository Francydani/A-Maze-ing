from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    valid = validate_ingredients(ingredients)
    if valid.endswith(" VALID"):
        return f"Spell recorded: {spell_name} ({valid})"
    else:
        return (
            "The spell has not been registered. "
            "Please enter valid ingredients."
        )
