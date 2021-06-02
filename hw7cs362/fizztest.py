import unittest
import fizz

class testCase(unittest.TestCase):
    def test1(self):
            self.assertEqual(fizz.buzz(), "Fizz")

if __name__ == "__main__":

    unittest.main()