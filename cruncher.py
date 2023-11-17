#!/usr/bin/env python3

import argparse
import logging

import character_mapping 
char_map = character_mapping.character_mapping()

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def generate_variations(input_string, current_index = 0, current_variation = ""):
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
    if char in char_map:
        for replacement in char_map[char]:
            new_variation = current_variation + replacement
            variations += generate_variations(
                input_string, current_index + 1, new_variation
            )
    else:
        variations += generate_variations(
            input_string, current_index + 1, current_variation + char
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

def main():
    """
    Main function to generate variations for the given input string.
    """
    parser = argparse.ArgumentParser(
        description="Generate variations of a string."
    )
    parser.add_argument(
        "input_string", help="The input string for generating variations."
    )
    parser.add_argument(
        "--output-file",
        "-o",
        help="Output file to save the variations. Default: variations.txt",
        default="variations.txt",
    )
    parser.add_argument(
        "--suffix",
        "-s",
        help="Suffix to add to variations. For example !!! will add !, !!, and !!! as possible \
        characters"
    )
    args = parser.parse_args()

    input_string = args.input_string
    logger.info("Input string: %s", input_string)
    if args.suffix:
        logger.info("Adding suffixes %s", str(list(args.suffix)))

    estimated_perms = estimate_permutations(input_string, char_map)
    logger.info("Estimated permutations: %s" % str(estimated_perms))

    all_variations = generate_variations(input_string)

    if args.suffix:
        total_variations = len(all_variations) * (len(args.suffix) + 2)
    else:
        total_variations = len(all_variations)
    logger.info("Total variations generated: %s", total_variations)

    output_file = args.output_file

    with open(output_file, "w", encoding="utf-8") as file:
        for index, variation in enumerate(all_variations):
            if (index + 1) % 100000 == 0 or index == total_variations - 1:
                logger.debug("Written %s variations.", index + 1)
            file.write(variation + "\n")
            if args.suffix:
                for i in range(len(args.suffix)+1):
                    suffix = args.suffix[0:i]
                    file.write(variation + suffix + "\n")

    logger.info("Variations written to %s", output_file)


if __name__ == "__main__":
    main()
