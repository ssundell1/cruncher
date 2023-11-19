#!/usr/bin/env python3
"""
Main module
"""

import argparse
import logging

import character_mapping
import generator

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    """
    Main function to generate variations for the given input string.
    """
    parser = argparse.ArgumentParser(description="Generate variations of a string.")
    parser.add_argument("input_string", help="The input string for generating variations.")
    parser.add_argument("--output-file","-o",
                        help="Output file to save the variations. Default: variations.txt",
                        default="variations.txt")
    args = parser.parse_args()

    character_map = character_mapping.character_mapping()

    logger.info("Input string: %s", args.input_string)

    estimated_perms = generator.estimate_permutations(args.input_string, character_map)
    logger.info("Estimated permutations: %s", str(estimated_perms))

    all_variations = generator.generate_variations(args.input_string, character_map)

    total_variations = len(all_variations)
    logger.info("Total variations generated: %s", total_variations)

    output_file = args.output_file

    with open(output_file, "w", encoding="utf-8") as file:
        for index, variation in enumerate(all_variations):
            if (index + 1) % 100000 == 0 or index == total_variations - 1:
                logger.debug("Written %s variations.", index + 1)
            file.write(variation + "\n")

    logger.info("Variations written to %s", output_file)


if __name__ == "__main__":
    main()
