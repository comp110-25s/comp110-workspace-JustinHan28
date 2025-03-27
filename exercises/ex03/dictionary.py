"""This is my code for ex03 that uses a dictionary"""

import pytest

__author__ = "730758899"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """inverts key and value pair in dictionary and checks for key duplicates"""
    values_set = []
    keys_list = list(input_dict.keys())  # makes a list of keys from the dict
    inverted = {}

    i = 0
    while i < len(keys_list):
        key = keys_list[i]
        value = input_dict[key]

        if (
            value in values_set
        ):  # if the iterated value is already within the set, there is a duplicate
            raise KeyError("Cannot invert dictionary since duplicate value exists")

        values_set.append(value)
        inverted[value] = key  # flips the key and value
        i += 1

    return inverted


with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)


def count(items: list[str]) -> dict[str, int]:
    """Counts frquency of each string in list"""
    result = {}
    i = 0
    while i < len(items):
        item = items[i]
        if item in result:  # if the item is already in the dict, add 1 to it
            result[item] += 1
        else:
            result[item] = (
                1  # if the item is not already in the dict, define it in the dict as value 1
            )
        i += 1
    return result


def favorite_color(name_colors: dict[str, str]) -> str:
    """Finds most frquent color in dictionary"""
    colors = list(name_colors.values())

    color_counts = count(colors)  # Count the occurrences of each color

    color_keys = list(color_counts.keys())
    i = 0
    max_count = 0
    most_common_color = ""

    while i < len(
        color_keys
    ):  # Find the color with the highest count using a while loop
        color = color_keys[i]
        color_count = color_counts[color]

        if color_count > max_count:
            max_count = color_count
            most_common_color = color

        i += 1

    return most_common_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    """Groups strings by length into a dictionary"""

    result = {}
    i = 0
    while i < len(strings):
        string = strings[i]
        length = len(string)

        if length in result:
            result[length].add(string)
        else:
            result[length] = {
                string
            }  # adds value to length key as a single string in a set

        i += 1

    return result
