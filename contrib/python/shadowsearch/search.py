import math
from typing import List, Union

from .models import Result
from .utils import char_count


SUPPORTED_ITEM_TYPES = Union[int, float, str]


def __check_if_items_match(item_1: SUPPORTED_ITEM_TYPES, item_2: SUPPORTED_ITEM_TYPES):
    if item_1 == item_2:
        return (True, 1)

    if type(item_1) is str and type(item_2) is str and (len(item_1) > 1 or len(item_2) > 1):
        item_1_char_count = char_count(item_1)
        item_2_char_count = char_count(item_2)

        combined_chars = set()

        unconsumed_chars = 0
        total_chars = 0

        for char in item_1_char_count:
            combined_chars.add(char)
        for char in item_2_char_count:
            combined_chars.add(char)

        for char in combined_chars:
            count_in_item_1 = item_1_char_count[char] if char in item_1_char_count else 0
            count_in_item_2 = item_2_char_count[char] if char in item_2_char_count else 0

            combined_count = count_in_item_1 + count_in_item_2

            unconsumed_chars += abs(count_in_item_1 - count_in_item_2)
            total_chars += combined_count

        percentage_match = 1 - (unconsumed_chars / max(len(item_1), len(item_2)))
        if percentage_match > 0.5:
            return (True, round(percentage_match, 1))

    return (False, None)


def binary_search(term: int, items: List[int]):
    raise NotImplementedError


def simple_search(term: SUPPORTED_ITEM_TYPES, items: List[SUPPORTED_ITEM_TYPES]):
    results = []

    for index in range(len(items)):
        item = items[index]
        match = __check_if_items_match(item, term)
        if match[0]:
            results.append(Result(index=index, value=item, confidence=match[1]))

    return results


def search_for_least_frequent_items(size: int, items: List[SUPPORTED_ITEM_TYPES]):
    raise NotImplementedError


def search_for_most_frequent_items(size: int, items: List[SUPPORTED_ITEM_TYPES]):
    raise NotImplementedError


def search_csv_file(filename: str, column: str, value: str):
    raise NotImplementedError
