#!/usr/bin/python3

import generator

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
    " ": [" ", "_", "-"],
}


def test_generate_variations_simple():
    assert generator.generate_variations("a", char_map) == ["a", "4", "@"]


def test_generate_variations_simple_negative():
    assert generator.generate_variations("a", char_map) != ["b", "4", "@"]


def test_generate_variations_medium():
    assert generator.generate_variations("Test", char_map) == [
        "Test",
        "Tes7",
        "Te5t",
        "Te57",
        "Te$t",
        "Te$7",
        "T3st",
        "T3s7",
        "T35t",
        "T357",
        "T3$t",
        "T3$7",
        "7est",
        "7es7",
        "7e5t",
        "7e57",
        "7e$t",
        "7e$7",
        "73st",
        "73s7",
        "735t",
        "7357",
        "73$t",
        "73$7",
    ]

def test_generate_variations_medium_negative():
    assert generator.generate_variations("Test", char_map) != [""]
