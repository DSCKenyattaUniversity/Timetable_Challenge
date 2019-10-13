# Timetable challenge using the Engineering school timetable
# by Koech A.

# engineering_timetable.xlsx used

import xlrd

# Setup constants
START_INDEX = 7
ROWS_PER_DAY = 8 # Except Thursdays which is 7
COLS_PER_HR = 2
ROWS_BEFORE_EACH_YEAR = 6
ROWS_AFTER_EACH_YEAR = 6

sheet = xlrd.open_workbook("engineering_timetable.xlsx").sheet_by_index(0)

def get_table_start_index(table_number):
    # Calculates the start index for a p
    #valid_start_indexes = [7, 59, 111, 163, 215, 267]
    
    if table_number > 6 or table_number < 0:
        print("Table number is out of range!")

    else:
        rows_taken_by_each_table = (ROWS_BEFORE_EACH_YEAR + 1 + (ROWS_PER_DAY * 5) -1  + ROWS_AFTER_EACH_YEAR) * (table_number - 1)
        table_start_index = rows_taken_by_each_table + ROWS_BEFORE_EACH_YEAR + 1

        return table_start_index


def get_day_index(table_number, indx, indy):
    # Returns the day and hour from given data parameters

    start_ind = get_table_start_index(table_number)
    # Calculate index of each row
    if indx == 0:
        day_ind = start_ind

    elif indx == 1:
        day_ind = start_ind + ROWS_PER_DAY

    elif indx == 2:
        day_ind = start_ind + (ROWS_PER_DAY * 2)

    elif indx == 3:
        day_ind = start_ind + (ROWS_PER_DAY * 3)

    else:
        day_ind = start_ind + (ROWS_PER_DAY * 4) - 1

    # Calculate index of each column
    col_indy = (indy * COLS_PER_HR) + 1

    return day_ind,col_indy


def check_if_cell_is_empty(rows, cols, x, d, h):
    # rows - number of rows for a particular day-hour
    # cols - number of cols of a particular day-hour
    EMPTY = True
    xy_ind = get_day_index(x,d,h)
    x_ind = xy_ind[0]

    for x in range(rows):
        y_ind = xy_ind[1]
        for y in range(cols):
            if not sheet.cell_type(x_ind, y_ind) == xlrd.XL_CELL_EMPTY:
                EMPTY = False
            y_ind += 1
        x_ind += 1

    return EMPTY

def get_day_and_hour(table_number, indx, indy):
    # Returns the day and hour from given data parameters

    start_ind = get_table_start_index(table_number)

    day_ind,col_indy = get_day_index(table_number, indx, indy)
    
    # Get hour of the day
    hour = sheet.cell_value(start_ind - 1, col_indy)
    
    if indx == 0:
        # Monday
        day = sheet.cell_value(day_ind, 0)

    elif indx == 1:
        # Tuesday
        day = sheet.cell_value(day_ind, 0)

    elif indx == 2:
        # Wednesday
        day = sheet.cell_value(day_ind, 0)

    elif indx == 3:
        # Thursday
        day = sheet.cell_value(day_ind, 0)

    else:
        # Friday
        day = sheet.cell_value(day_ind, 0)

    return f"{day} {hour}"

def free_hours(n):
    # Returns a list of day and free hours 
    free_hours_array = []
    start_ind = get_table_start_index(n)

    for day in range(5):
        for hour in range(12):

            if day == 3:
                ROWS = 7
            else:
                ROWS = ROWS_PER_DAY

            isEmpty = check_if_cell_is_empty(ROWS, COLS_PER_HR, n, day, hour)
            if isEmpty == True:
                day_hr = get_day_and_hour(n, day, hour)
                free_hours_array.append(day_hr)

    return free_hours_array


def display(free_hours_array):
    print(len(free_hours_array)," Hrs are free")
    print("The Free Hours are:")
    print("="*50)
    print(free_hours_array)
    print("="*50)


def check_free_hours(*args):
    # args are the table numbers
    no_of_args = len(args)

    if no_of_args == 1:
        # Single table passed in
        free_hours_array = free_hours(args[0])
        display(free_hours_array)

    elif no_of_args == 2:
        # Two tables passed in
        arr_1 = free_hours(args[0])
        arr_2 = free_hours(args[1])

        arr_3 = []
        for x in arr_1:
            for y in arr_2:
                if x == y:
                    arr_3.append(x)

        display(arr_3)
    
    elif no_of_args == 3:
        # Three tables passed in
        arr_1 = free_hours(args[0])
        arr_2 = free_hours(args[1])
        arr_3 = free_hours(args[2])

        arr_4 = []
        for x in arr_1:
            for y in arr_2:
                for z in arr_3:
                    if x == y == z:
                        arr_4.append(x)
                    
        display(arr_4)
    
    elif no_of_args == 4:
        # Three tables passed in
        arr_1 = free_hours(args[0])
        arr_2 = free_hours(args[1])
        arr_3 = free_hours(args[2])
        arr_4 = free_hours(args[3])

        arr_5 = []
        for x in arr_1:
            for y in arr_2:
                for z in arr_3:
                    for a in arr_4:
                        if x == y == z == a:
                            arr_5.append(x)
                    
        display(arr_5)
    
    elif no_of_args == 5:
       # Three tables passed in
        arr_1 = free_hours(args[0])
        arr_2 = free_hours(args[1])
        arr_3 = free_hours(args[2])
        arr_4 = free_hours(args[3])
        arr_5 = free_hours(args[4])

        arr_6 = []
        for x in arr_1:
            for y in arr_2:
                for z in arr_3:
                    for a in arr_4:
                        for b in arr_5:
                            if x == y == z == a == b:
                                arr_6.append(x)
                    
        display(arr_6)
    
    elif no_of_args == 6:
        # Three tables passed in
        arr_1 = free_hours(args[0])
        arr_2 = free_hours(args[1])
        arr_3 = free_hours(args[2])
        arr_4 = free_hours(args[3])
        arr_5 = free_hours(args[4])
        arr_6 = free_hours(args[5])

        arr_7 = []
        for x in arr_1:
            for y in arr_2:
                for z in arr_3:
                    for a in arr_4:
                        for b in arr_5:
                            for c in arr_6:
                                if x == y == z == a == b == c:
                                    arr_7.append(x)
                    
        display(arr_7)
    
    else:
        print(" Arguments exceed number of tables!")


if __name__ == "__main__":
    print("\n\nTable 1")
    check_free_hours(1)

    print("\n\nTable 2 and 6")
    check_free_hours(2,6)

    print("\n\nTable 1 and 2")
    check_free_hours(1,2)

    print("\n\nTable 1,2 and 3")
    check_free_hours(1,2,3)

    print("\n\nTable 2,4 and 5")
    check_free_hours(2,4,5)

    print("\n\nTable 2,3,4,5 and 6")
    check_free_hours(2,3,4,5,6) # Takes some time

    #print("\n\nTable 1,2,3,4,5 and 6")
    #check_free_hours(2,3,4,5,6,1) # Takes time, high computing power

