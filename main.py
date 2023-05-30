from gochujang_recipes import gochujang_recipes


def force_same_keys(recipes: dict) -> None:
    """
    Forces all recipes to have the same keys
    :param recipes: dictionary of dictionaries representing recipes
    :return: None
    """
    all_ingredients = [set(d.keys()) for d in recipes.values()]
    all_ingredients = set().union(*all_ingredients)
    for recipe in recipes:
        for ingredient in all_ingredients:
            recipes[recipe].setdefault(ingredient, 0)


def scale_recipe(recipe: dict, desired_total: int = 1000) -> dict:
    """
    Scales a recipe to a desired total
    :param recipe: dictionary of ingredients and amounts
    :param desired_total: desired total amount
    :return: dictionary of ingredients and scaled amounts
    """
    total: float = sum(recipe.values())
    scale: float = desired_total / total
    return {k: v * scale for k, v in sorted(recipe.items())}


def format_recipes(recipes: dict) -> list:
    """
    Prints out the recipes in Reddit table format
    :param recipes: dictionary of recipes
    :return: None
    """
    first_recipe: dict = recipes[list(recipes.keys())[0]]
    lines = [
        ' | '.join(['...'] + list(recipes.keys())),
        '|'.join([":--"] + ["--:"] * (len(recipes.keys())))
    ]
    for ingredient in first_recipe.keys():
        line: list = [ingredient]
        for recipe in recipes.keys():
            line.append(f"{recipes[recipe][ingredient]:.2f}g")
        lines.append(' | '.join(line))
    return lines


def main():
    force_same_keys(gochujang_recipes)
    scaled_recipes: dict = {}
    for key in gochujang_recipes:
        scaled_recipes[key] = scale_recipe(gochujang_recipes[key], 1000)
    output: list = format_recipes(scaled_recipes)
    print('\n'.join(output))


if __name__ == '__main__':
    main()
