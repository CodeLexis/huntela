import itertools
from collections import Counter


def char_count(s):
    """
    Returns a dictionary mapping each character in a string to the number of times it appears.

    Args:
        s (str): Input string.

    Returns:
        dict: Dictionary mapping each character to the number of times it appears.
    """

    char_dict = {}
    for char, count in Counter(itertools.chain.from_iterable(s)).items():
        char_dict[char] = count

    return char_dict
