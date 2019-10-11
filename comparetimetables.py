# Implementation of the timetable challenge in Py
# By: Koech A.
# Email: koecha00@gmail.com

"""
>> Assumptions taken:
    + Timetable is saved as an Excel Sheet
    + Timetable data is compact with no empty rows or colums in between as shown below

           column 1     col 2    col3      col 4       col 5                                                                                 col 13
        -------------+---------+---------+----------+-----------+-----------+----------+---------+---------+---------+---------+---------+---------+
 row 1  | Day        | 7-8 AM  | 8-9 AM  | 9-10 AM  | 10-11 AM  | 11-12 PM  | 12-1 PM  | 1-2 PM  | 2-3 PM  | 3-4 PM  | 4-5 PM  | 5-6 PM  | 6-7 PM  |
        +------------+---------+---------+----------+-----------+-----------+----------+---------+---------+---------+---------+---------+---------+
 row 2  | Monday     |         |         |          |           |           |          |         |         |         |         |         |         |
        +------------+---------+---------+----------+-----------+-----------+----------+---------+---------+---------+---------+---------+---------+
 row 3  | Tuesday    |         |         |          |           |           |          |         |         |         |         |         |         |
        +------------+---------+---------+----------+-----------+-----------+----------+---------+---------+---------+---------+---------+---------+
 row 4  | Wednesday  |         |         |          |           |           |          |         |         |         |         |         |         |
        -------------+---------+---------+----------+-----------+-----------+----------+---------+---------+---------+---------+---------+---------+
 row 5  | Thursday   |         |         |          |           |           |          |         |         |         |         |         |         |
        -------------+---------+---------+----------+-----------+-----------+----------+---------+---------+---------+---------+---------+---------+
 row 6  | Friday     |         |         |          |           |           |          |         |         |         |         |         |         |
        -------------+---------+---------+----------+-----------+-----------+----------+---------+---------+---------+---------+---------+---------+

"""

# xlrd is a module for reading excel files
# pip install xlrd
import xlrd

class Data():
    """ 
    This Class takes in an Excel file, reads through the cells and returns the empty cells
        > dt = Data("filename.xlsx)
        > dt.read_tables() #Returns a list of the empty slots of the timetable
    """
    def __init__(self,table):
        self.table = table
        
        self.empty_cells = [] # To hold data of empty cells

    def read_tables(self):
        sheet = xlrd.open_workbook(self.table).sheet_by_index(0)

        # Use sheet.cell_value(row,col) to read cell contents
        # Get number of rows and columns
        rows = sheet.nrows
        cols = sheet.ncols

        # Iterate over the sheet and collect all empty slots on an array
        for r in range(rows):
            for c in range(cols):
                # Check if cell is empty
                # If empty get the slot's day and time

                if sheet.cell_type(r,c) == xlrd.XL_CELL_EMPTY:
                    day = f"{sheet.cell_value(r,0)} {sheet.cell_value(0,c)}"
                    self.empty_cells.append(day)
        
        return self.empty_cells

def compare(*args):
    # *args should be valid xls files of any number
    """
    Takes in Excel files of any number, currently can handle a max of 2, and 
    passes it to the Data class. It then outputs the common slots in both 
    excel timetables

    Usage:
        > compare("filename.xlsx")
        #prints a list
        > compare("filea.xlsx","fileb.xlsx")
        #prints a list
    """

    n = len(args)
    
    if n == 0:
        print("No File specified")

    elif n == 1:
        dt1 = Data(args[0]).read_tables()
        print("\nFree hours")
        print("="*10)
        print(dt1)

    elif n == 2:
        print("\nFree hours")
        print("="*10)
        dt1 = Data(args[0]).read_tables()
        dt2 = Data(args[1]).read_tables()
        print(set(dt1).intersection(dt2))

        arr_x = []
        for x in dt1:
            for y in dt2:
                if x == y:
                    arr_x.append(x)
        
        print("\nFree hours")
        print("="*10)
        print(arr_x)
        

    else:
        print("Handle the rest")



compare("tmtbl1.xlsx")
compare("tmtbl2.xlsx")
compare("tmtbl1.xlsx", "tmtbl2.xlsx")