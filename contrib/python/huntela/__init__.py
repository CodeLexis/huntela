"""Search of items easily in Python

The module contains the following functions:

- `binary_search(term, items, key = None)` - Result: A Result object representing the search result, or None if it is not found.
- `simple_search(term, items, key = None)` - List[Result]: A list of Result objects representing the search results.
- `search_for_least_frequent_items(size, items, key = None)` - List[Result]: A list of the specified size containing the least frequent item(s)
- `search_for_most_frequent_items(size, items, key = None)` - List[Result]: A list of the specified size containing the most frequent item(s)
"""


from .search import (
  binary_search,
  search_for_least_frequent_items,
  search_for_most_frequent_items,
  simple_search
)
