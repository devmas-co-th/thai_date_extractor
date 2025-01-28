import unittest
from thai_date_extractor import extract_date_range_from_query

class TestDateExtractor(unittest.TestCase):
    def test_today(self):
        query = "รายงานประจำวันนี้"
        result = extract_date_range_from_query(query)
        self.assertEqual(result['start_date'], result['end_date'])

    def test_date_range(self):
        query = "รายงานตั้งแต่ 01/01/2025 ถึง 31/12/2025"
        result = extract_date_range_from_query(query)
        self.assertEqual(result['start_date'], '2025-01-01')
        self.assertEqual(result['end_date'], '2025-12-31')

    def test_thai_numbers(self):
        query = "รายงานตั้งแต่ ๑๕/๐๑/๒๕๖๗ ถึง ๒๐/๐๑/๒๕๖๗"
        result = extract_date_range_from_query(query)
        self.assertEqual(result['start_date'], '2024-01-15')
        self.assertEqual(result['end_date'], '2024-01-20')
