import unittest
import leap

class testCase(unittest.TestCase):
    def test1(self):
            self.assertEqual(leap.leapyr(2020),  (2020, "is a leap year!!"))

if __name__ == "__main__":

    unittest.main()
