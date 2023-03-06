# Huntela
**Huntela** makes searching in Python very simple.

```python
>>> import huntela
>>> huntela.simple_search("app", ["app", "apple", "hello", "world"])
[
    {'confidence': 1, 'index': 0, 'value': 'app'},
    {'confidence': 0.6, 'index': 1, 'value': 'apple'}
]
>>> huntela.binary_search(term='a', items=['a', 'b', 'c'])
{'confidence': 1, 'index': 0, 'value': 'a'}
>>> huntela.binary_search(term='a', items=['a', 'b', 'c'])
{'confidence': 1, 'index': 0, 'value': 'a'}
>>> huntela.search_for_least_frequent_items(size=1, ['a', 'b', 'a', 'e', 'a', 'e'])
[{'confidence': 1, 'index': None, 'value': 'b'}]
```

With a variety of algorithms to choose from, finding what you're looking for has never been easier.

From binary search to linear search and more, Huntela has everything you need to 
quickly and efficiently search through your data. With a simple, intuitive interface
and lightning-fast performance, Huntela is the go-to package for anyone who needs to search through data.

Whether you're a data scientist, engineer, or  developer, Huntela will help you find what you need.

## Installation

> Huntela officially supports Python 3.9 upwards. 

Huntela is available on PyPi and it can be installed using `pip`

```batch
python -m pip install huntela
```