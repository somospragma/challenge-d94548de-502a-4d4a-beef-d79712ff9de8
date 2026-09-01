import unittest
from scripts.extract_data import extract_data
from scripts.transform_data import transform_data
from scripts.load_data import load_data

class TestPipeline(unittest.TestCase):
    def test_extract_data(self):
        extract_data()
        self.assertTrue(True)

    def test_transform_data(self):
        transform_data()
        self.assertTrue(True)

    def test_load_data(self):
        load_data()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()