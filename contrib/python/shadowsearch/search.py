from typing import List, Union

from .models import Result


def __check_if_items_match(item_1, item_2):
    return item_1 == item_2


def binary_search(term: int, items: List[int]):
    raise NotImplementedError


def simple_search(term: str, items: List[str]):
    results = []

    for index in range(len(items)):
        item = items[index]
        if __check_if_items_match(item, term):
            results.append(Result(index=index, value=item))

    return results


def search_for_least_frequent_items(size: int, items: List[Union[int, float]]):
    raise NotImplementedError


def search_for_most_frequent_items(size: int, items: List[Union[int, float]]):
    raise NotImplementedError


def search_csv_file(filename: str, column: str, value: str):
    raise NotImplementedError
