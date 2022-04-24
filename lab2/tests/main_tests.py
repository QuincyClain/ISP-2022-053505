import math
import unittest
from main import fa
from main import fact


class TestMain(unittest.TestCase):
    def test_fa(self):
        self.expected_val = 0.30446608
        self.actual_val = fa(10)
        self.assertAlmostEqual(self.expected_val, self.actual_val)

    def test_fact(self):
        self.expected_val = 120
        self.actual_val = fact(5)
        self.assertEqual(self.expected_val, self.actual_val)


if __name__ == '__main__':
    unittest.main()