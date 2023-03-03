import unittest

from shadowsearch import simple_search


class SimpleSearch(unittest.TestCase):
    def test_missing_term(self):
        results = simple_search(term='a', items=[])
        self.assertEqual(len(results), 0, 'Missing term does not return empty results')

    def test_string_search(self):
        results = simple_search(term='a', items=['a', 'b', 'c'])
        self.assertEqual(len(results), 1, 'Term returns at least one matching result')

    def test_result_structure(self):
        results = simple_search(term='a', items=['a', 'b', 'c'])
        self.assertIsInstance(results[0], dict)

    def test_result_content(self):
        results = simple_search(term='a', items=['a', 'b', 'c'])
        self.assertEqual(results[0]['index'], 0)
        self.assertEqual(results[0]['value'], 'a')
        self.assertNotEqual(results[0]['index'], 1)
        self.assertNotEqual(results[0]['value'], 'b')


if __name__ == '__main__':
    unittest.main()
