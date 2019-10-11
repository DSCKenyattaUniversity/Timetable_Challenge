import unittest

from comparetimetables import Data

class TestData(unittest.TestCase):
    def test_data(self):
        
        empty1 = ['MONDAY 8-9 AM', 'MONDAY 9-10 AM', 'MONDAY 10-11 AM', 'MONDAY 11-12 PM', 'MONDAY 1-2 PM', 'MONDAY 2-3 PM', 'MONDAY 5-6 PM', 'MONDAY 6-7 PM', 'TUESDAY 7-8 AM', 'TUESDAY 10-11 AM', 'TUESDAY 11-12 PM', 'TUESDAY 12-1 PM', 'TUESDAY 1-2 PM', 'TUESDAY 2-3 PM', 'TUESDAY 3-4 PM', 'TUESDAY 4-5 PM', 'TUESDAY 5-6 PM', 'WEDNESDAY 7-8 AM', 'WEDNESDAY 8-9 AM', 'WEDNESDAY 9-10 AM', 'WEDNESDAY 10-11 AM', 'WEDNESDAY 12-1 PM', 'WEDNESDAY 2-3 PM', 'WEDNESDAY 3-4 PM', 'WEDNESDAY 4-5 PM', 'WEDNESDAY 5-6 PM', 'WEDNESDAY 6-7 PM', 'THURSDAY 8-9 AM', 'THURSDAY 11-12 PM', 'THURSDAY 12-1 PM', 'THURSDAY 1-2 PM', 'THURSDAY 5-6 PM', 'THURSDAY 6-7 PM', 'FRIDAY 7-8 AM', 'FRIDAY 8-9 AM', 'FRIDAY 9-10 AM', 'FRIDAY 10-11 AM', 'FRIDAY 12-1 PM', 'FRIDAY 1-2 PM', 'FRIDAY 2-3 PM', 'FRIDAY 3-4 PM', 'FRIDAY 6-7 PM']
        dt1 = Data("tmtbl1.xlsx").read_tables()
        self.assertCountEqual(dt1,empty1)

    def test_compare(self):

        empty = ['MONDAY 9-10 AM', 'MONDAY 10-11 AM', 'MONDAY 11-12 PM', 'MONDAY 2-3 PM', 'MONDAY 5-6 PM', 'MONDAY 6-7 PM', 'TUESDAY 11-12 PM', 'TUESDAY 12-1 PM', 'TUESDAY 2-3 PM', 'TUESDAY 3-4 PM', 'WEDNESDAY 7-8 AM', 'WEDNESDAY 10-11 AM', 'WEDNESDAY 12-1 PM', 'WEDNESDAY 2-3 PM', 'WEDNESDAY 3-4 PM', 'WEDNESDAY 5-6 PM', 'WEDNESDAY 6-7 PM', 'THURSDAY 8-9 AM', 'THURSDAY 11-12 PM', 'THURSDAY 5-6 PM', 'THURSDAY 6-7 PM', 'FRIDAY 8-9 AM', 'FRIDAY 12-1 PM', 'FRIDAY 1-2 PM', 'FRIDAY 2-3 PM', 'FRIDAY 3-4 PM', 'FRIDAY 6-7 PM']
    
        dt1 = Data("tmtbl1.xlsx").read_tables()
        dt2 = Data("tmtbl2.xlsx").read_tables()
        dt = set(dt1).intersection(dt2)

        self.assertCountEqual(dt,empty)

        
if __name__ == "__main__":
    unittest.main()