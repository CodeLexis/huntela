from typing import List, Union

from models import Result


def simple_search(term: str, items: List[str]):
    results = []

    for index in range(len(items)):
        item = items[index]
        if item == term:
            results.append(
                Result(index=index, item=item)
            )

    return results


def search_for_least_frequent_items(size: int, items: List[Union[int, float]]):
    return


def search_for_most_frequent_items(size: int, items: List[Union[int, float]]):
    return
