from gochujang_recipes import gochujang_recipes


def assert_same_keys(dict_of_dicts: dict) -> None:
    """
    Asserts that all the dictionaries in a dictionary
        of dictionaries all have the same keys
    :param dict_of_dicts: dictionary of dictionaries
    :return: None
    """
    dict_keys = [set(d.keys()) for d in dict_of_dicts.values()]
    first_keys_set: set = dict_keys[0]
    for keys_set in dict_keys[1:]:
        assert keys_set == first_keys_set, \
            "Dictionaries have different keys"


def scale_recipe(recipe: dict, desired_total: int) -> dict:
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
        ' | '.join([''] + list(recipes.keys())),
        '|'.join([":--"] + ["--:"] * (1 + len(recipes.keys())))
    ]
    for ingredient in first_recipe.keys():
        line: list = [ingredient]
        for recipe in recipes.keys():
            line.append(f"{recipes[recipe][ingredient]:.2f}g")
        lines.append(' | '.join(line))
    return lines


if __name__ == '__main__':
    assert_same_keys(gochujang_recipes)
    scaled_recipes: dict = {}
    for key in gochujang_recipes:
        scaled_recipes[key] = scale_recipe(gochujang_recipes[key], 1000)
    output: list = format_recipes(scaled_recipes)
    print('\n'.join(output))
