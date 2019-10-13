import unittest

from timetable import free_hours as fh

class TestData(unittest.TestCase):
    def test_one(self):
        dt = len(fh(1))
        self.assertEquals(dt,36)

    def test_two(self):

        dt = len(fh(3))
        self.assertEquals(dt,36)

    def test_five(self):

        dt = len(fh(6))
        self.assertEquals(dt,34)

        
if __name__ == "__main__":
    unittest.main()