import unittest

from shadowsearch import simple_search


class SimpleSearch(unittest.TestCase):
    def test_missing_term(self):
        results = simple_search(term='a', items=[])
        self.assertEqual(len(results), 0, 'Missing term does not return empty results')

    def test_string_search(self):
        results = simple_search(term='a', items=['a', 'b', 'c'])
        self.assertEqual(len(results), 1, 'Search does not return exactly one matching result for single character strings')

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
        self.assertEqual(results[0]['index'], 0)
        self.assertEqual(results[0]['value'], 'a')
        self.assertEqual(results[0]['confidence'], 1)

        self.assertNotEqual(results[0]['index'], 1)
        self.assertNotEqual(results[0]['value'], 'b')
        self.assertNotEqual(results[0]['confidence'], 0)


if __name__ == '__main__':
    unittest.main()
