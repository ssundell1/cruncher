"""
Generator functions for cruncher
"""

def generate_variations(input_string, character_map, current_index = 0, current_variation = ""):
    """
    Generate all possible variations of the given input string and the global char map.

    Parameters:
        input_string (str): The input string to generate leet speak variations for.

    Returns:
        list: A list of strings containing speak variations.
    """
    if current_index == len(input_string):
        return [current_variation]

    char = input_string[current_index]
    variations = []
    if char in character_map:
        for replacement in character_map[char]:
            new_variation = current_variation + replacement
            variations += generate_variations(
                input_string, character_map, current_index + 1, new_variation
            )
    else:
        variations += generate_variations(
            input_string, character_map, current_index + 1, current_variation + char
        )

    return variations

def estimate_permutations(input_string, character_map):
    """
    Quickly estimate the number of permutations for the given input string and character map.

    Parameters:
        input_string (str): The input string to estimate permutations for.
        character_map (dict): The character map dictionary.

    Returns:
        int: The estimated number of permutations.
    """
    permutations_estimate = 1
    for char in input_string:
        if char in character_map:
            permutations_estimate *= len(character_map[char])
    return permutations_estimate
