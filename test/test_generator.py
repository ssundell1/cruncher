#!/usr/bin/python3
"""
Test function for the generator module
"""

import generator

char_map = {
    "a": ["a", "4"],
    "A": ["A", "", "@"],
    "e": ["E", "e", "3"],
    "E": ["E", "3"],
    "i": ["I", "i", "1", "!"],
    "I": ["I", "1", "!"],
    "o": ["O", "o", "0"],
    "O": ["O", "0"],
    "s": ["s", "5"],
    "S": ["S", "5", "$"],
    "t": ["T", "t", "7"],
    "T": ["T", "7"],
    "z": ["z", "2"],
    "Z": ["Z", "2"],
    " ": [" ", "_", "-"],
}


def test_generate_variations_simple():
    """
    Test variation generator function using a simple positive test
    """
    assert generator.generate_variations("a", char_map) == ["a", "4",]


def test_generate_variations_simple_negative():
    """
    Test variation generator function using a simple negative test
    """
    assert generator.generate_variations("a", char_map) != ["b", "4", "@"]


def test_generate_variations_medium():
    """
    Test variation generator function using a medium positive test
    """
    assert generator.generate_variations("Yes", char_map) == [
        "YEs",
        "YE5",
        "Yes",
        "Ye5",
        "Y3s",
        "Y35"
    ]

def test_generate_variations_medium_negative():
    """
    Test variation generator function using a medium negative test
    """
    assert generator.generate_variations("Test", char_map) != [""]
