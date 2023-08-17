#!/usr/bin/env python3

import argparse
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Leet speak dictionary
char_map = {
    "a": ["a", "4", "@"],
    "A": ["A", "4", "@"],
    "e": ["e", "3"],
    "E": ["E", "3"],
    "i": ["i", "1", "!"],
    "I": ["I", "1", "!"],
    "o": ["o", "0"],
    "O": ["O", "0"],
    "s": ["s", "5", "$"],
    "S": ["S", "5", "$"],
    "t": ["t", "7"],
    "T": ["T", "7"],
    "z": ["z", "2"],
    "Z": ["Z", "2"],
    " ": [" ", "_", "-"]
}


def generate_variations(input_string):
    """
    Generate all possible variations of the given input string and the global char map.

    Parameters:
        input_string (str): The input string to generate leet speak variations for.

    Returns:
        list: A list of strings containing speak variations.
    """

    def generate_variation(input_string, current_index, current_variation):
        if current_index == len(input_string):
            return [current_variation]

        char = input_string[current_index]
        variations = []
        if char in char_map:
            for replacement in char_map[char]:
                new_variation = current_variation + replacement
                variations += generate_variation(
                    input_string, current_index + 1, new_variation
                )
        else:
            variations += generate_variation(
                input_string, current_index + 1, current_variation + char
            )

        return variations

    all_variations = generate_variation(input_string, 0, "")
    return all_variations


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
    logger.info("Adding suffixes %s", str(list(args.suffix)))

    all_variations = generate_variations(input_string)

    if args.suffix:
        total_variations = len(all_variations) * (len(args.suffix) + 2)
    else:
        total_variations = len(all_variations)
    logger.info("Total variations to be generated: %s", total_variations)

    output_file = args.output_file

    with open(output_file, "w", encoding="utf-8") as file:
        for index, variation in enumerate(all_variations):
            if (index + 1) % 100000 == 0 or index == total_variations - 1:
                logger.info("Generated %s variations.", index + 1)
            file.write(variation + "\n")
            if args.suffix:
                for i in range(len(args.suffix)+1):
                    suffix = args.suffix[0:i]
                    file.write(variation + suffix + "\n")

    logger.info("Variations written to %s", output_file)


if __name__ == "__main__":
    main()
