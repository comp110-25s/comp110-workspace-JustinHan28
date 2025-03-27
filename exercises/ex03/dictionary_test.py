"""This is the test code for my ex03 for my dictionary"""

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len

__author__ = "730758899"


def test_invert_regular_case():
    """
    Test invert with a regular dictionary with unique values.
    """
    test_dict = {"a": "z", "b": "y", "c": "x"}
    expected = {"z": "a", "y": "b", "x": "c"}
    assert invert(test_dict) == expected


def test_invert_single_item():
    """
    Test invert with a dictionary containing only one key-value pair.
    """
    test_dict = {"apple": "cat"}
    expected = {"cat": "apple"}
    assert invert(test_dict) == expected


def test_invert_duplicate_values():
    """
    Test invert raises KeyError when the dictionary has duplicate values.
    Edge case: Dictionary containing duplicate values should raise KeyError.
    """
    test_dict = {"kris": "jordan", "michael": "jordan"}
    try:
        invert(test_dict)
        assert False, "Expected KeyError was not raised"
    except KeyError:
        assert True


def test_count_regular_case():
    """Test count with a list containing some duplicate strings."""
    test_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    expected = {"apple": 3, "banana": 2, "cherry": 1}
    assert count(test_list) == expected


def test_count_empty_list():
    """
    Test count with an empty list.
    Edge case: Empty list should return empty dictionary.
    """
    assert count([]) == {}


def test_count_single_element():
    """Test count with a list containing a single element."""
    assert count(["apple"]) == {"apple": 1}


def test_favorite_color_clear_winner():
    """Test favorite_color with a clear most common color."""
    test_dict = {
        "Alice": "blue",
        "Bob": "red",
        "Charlie": "blue",
        "David": "green",
        "Eve": "blue",
    }
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_tie():
    """
    Test favorite_color when there's a tie for the most common color.
    Edge case: Returns the first encountered color.
    """
    test_dict = {"Alice": "blue", "Bob": "red", "Charlie": "blue", "David": "red"}

    assert favorite_color(test_dict) in ["blue", "red"]


def test_favorite_color_single_entry():
    """Test favorite_color with only one entry."""
    test_dict = {"Alice": "purple"}
    assert favorite_color(test_dict) == "purple"


def test_bin_len_regular_case():
    """Test bin_len with a list of strings of different lengths."""
    test_list = ["the", "quick", "fox"]
    expected = {3: {"the", "fox"}, 5: {"quick"}}
    assert bin_len(test_list) == expected


def test_bin_len_with_duplicates():
    """Test bin_len with duplicate strings."""
    test_list = ["the", "the", "fox"]
    expected = {3: {"the", "fox"}}
    assert bin_len(test_list) == expected


def test_bin_len_empty_list():
    """
    Test bin_len with an empty list.
    Edge case: Empty list should return empty dictionary.
    """
    assert bin_len([]) == {}
