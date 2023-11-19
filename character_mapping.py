"""
Module for configuring the character substitution map to use
"""

def character_mapping():
    """
    Substitution dictionary
    Change this to modify possible characters for each original character
    """
    return {
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
