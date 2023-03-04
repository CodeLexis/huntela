import unittest

from huntela import binary_search, search_for_least_frequent_items, simple_search


class BinarySearchTest(unittest.TestCase):
    def test_missing_term(self):
        result = binary_search(term=5, items=[])
        self.assertIsNone(result, 'Missing term does not return empty results')

    def test_integer_search(self):
        result = binary_search(term=5, items=[1, 5, 10, 15, 20])
        self.assertEqual(result['confidence'], 1)
        self.assertEqual(result['index'], 1)
        self.assertEqual(result['value'], 5)

    def test_string_search(self):
        result = binary_search(term='a', items=['a', 'b', 'c'])
        self.assertEqual(result['confidence'], 1)
        self.assertEqual(result['index'], 0)
        self.assertEqual(result['value'], 'a')


class SimpleSearchTest(unittest.TestCase):
    def test_missing_term(self):
        results = simple_search(term='a', items=[])
        self.assertEqual(len(results), 0, 'Missing term does not return empty results')

    def test_string_search(self):
        results = simple_search(term='a', items=['a', 'b', 'c'])
        self.assertEqual(len(results), 1, 'Search does not return exactly one matching result for single character strings')

    def test_integer_search(self):
        results = simple_search(term=2, items=[1, 2, 3])
        self.assertEqual(len(results), 1, 'Search does not return exactly one matching result for integers')

    def test_string_search_fuzzy(self):
        results = simple_search(term='apple', items=['pap', 'app', 'le', 'applet'])
        self.assertEqual(len(results), 3, 'Search does not return exactly one matching result for multi-character strings')
        self.assertEqual(results[0]['confidence'], 0.6, 'Search did not return the expected confidence rating')
        self.assertEqual(results[1]['confidence'], 0.6, 'Search did not return the expected confidence rating')
        self.assertEqual(results[2]['confidence'], 0.8, 'Search did not return the expected confidence rating')

    def test_result_structure(self):
        results = simple_search(term='a', items=['a', 'b', 'c'])
        self.assertIsInstance(results[0], dict)

    def test_result_content(self):
        results = simple_search(term='a', items=['a', 'b', 'c'])
        self.assertEqual(results[0]['confidence'], 1)
        self.assertEqual(results[0]['index'], 0)
        self.assertEqual(results[0]['value'], 'a')

        self.assertNotEqual(results[0]['confidence'], 0)
        self.assertNotEqual(results[0]['index'], 1)
        self.assertNotEqual(results[0]['value'], 'b')


class LeastFrequentElementsSearchTest(unittest.TestCase):
    def test_one(self):
        results = search_for_least_frequent_items(1, [1, 2, 1, 5, 1, 5])
        self.assertEqual(len(results), 1)

    def test_two(self):
        results = search_for_least_frequent_items(2, [1, 2, 1, 5, 1, 5])
        self.assertEqual(len(results), 2)


if __name__ == '__main__':
    unittest.main()
