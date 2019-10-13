from timetable import TimeTable 


timetable1 = TimeTable()
timetable2 = TimeTable()

timetable2.monday = ["7to 12" , "13 to 15", "16 to 18"]
timetable2.tuesday = ["7 to 9" , "14 to 16", "17 to 18"]
timetable2.wednesday = ["8 to 10" , "14 to 16" , "17 to 18"]
timetable2.thursday = ["7 to 9" , "9 to 12" , "13 to 15","17 to 18"]
timetable2.friday = ["9 to 11" , "13 to 15" , "17 to 18"]
timetable2.add_all()

timetable1.tuesday = ["7to 12" , "13 to 15", "16 to 18"]
timetable1.monday = ["7 to 9" , "14 to 16", "17 to 18"]
timetable1.wednesday = ["8 to 10" , "14 to 16" , "17 to 18"]
timetable1.friday = ["7 to 9" , "9 to 12" , "13 to 15","17 to 18"]
timetable1.thursday = ["9 to 11" , "13 to 15" , "17 to 18"]
timetable1.add_all()



NUMBER_OF_HOURS = 11 # number of all one hour periods from 7 to 18hrs
hour_taken_array = []

# initialize hour_taken_array to zeros
for one_hour_period in range(NUMBER_OF_HOURS):
    hour_taken_array.append(0)

# used to fill the hour_taken_array
mappings = {
        "7 to 8" : 0,
        "8 to 9" : 1,
        "9 to 10" : 2,
        "10 to 11" : 3,
        "11 to 12" : 4,
        "12 to 13" : 5,
        "13 to 14" : 6,
        "14 to 15" : 7,
        "15 to 16" : 8,
        "16 to 17" : 9,
        "17 to 18" : 10,
        }


hours_string_prompt = ""

for hour in range(7,19):
    hours_string_prompt = hours_string_prompt + str(hour) + "\t"

# used in deciding how many '|' to print
now_multiplier = 1
next_multiplier = 1



# an array of one_hour_slots of the whole week
array_of_one_hour_slots_of_week = []

for day in range(5):
    array_of_one_hour_slots_of_week.append([])

    for one_hour_period in range(NUMBER_OF_HOURS):
        array_of_one_hour_slots_of_week[day].append(0)



# split the scheduled periods to one hour periods
def split_into_one_hour_components( day_schedule ):
    
    # arrays to store the one hour periods
    schedule_time_pairs = []

    for schedule in day_schedule:
        # first split into given hours
        timeScheduleList = schedule.split("to")
        startHour = int( timeScheduleList[0])
        finishHour = int( timeScheduleList[-1])

        if finishHour - startHour > 1:
            # need to create new strings
            lesson_length = finishHour - startHour
            this_hour = startHour
            for hour in range(lesson_length):

                next_hour = this_hour + 1
                new_schedule_time = str(this_hour) + " to " + str(next_hour) #create a new hour string
                schedule_time_pairs.append(new_schedule_time)

                this_hour = next_hour
        else:
            schedule_time_pairs.append(schedule)


   # for time_pair in schedule_time_pairs:
   #     print(time_pair)

    return schedule_time_pairs



def map_one_hour_slots_to_hour_taken_array( scheduled_one_hour_time, hour_taken_array):
    

    for one_hour_period in scheduled_one_hour_time:

       index_in_hours_taken_array = mappings.get( one_hour_period , "Invalid hour")
       hour_taken_array[ index_in_hours_taken_array ] = 1




# Takes in array whose element represents if a particular our is taken
print_once = True
tabs_before_printing_hours_string_prompt ='\t\t'
tabs_before_printing_day_to_screen ='\t\t'
def print_hour_string_before_timetable():
    global print_once
    if print_once:
        print_once = False
        print(tabs_before_printing_hours_string_prompt +  hours_string_prompt)

def print_a_timetable_to_the_terminal( hour_taken_array):
    global next_multiplier
    global now_multiplier
    global tabs_before_printing_day_to_screen
    global tabs_before_printing_hours_string_prompt
    shade = ""

    previous_hour_free= False

    for index,hour_taken in enumerate(hour_taken_array):

        # if there is a 7 to 8 class 
        if hour_taken_array[0] == 1:

            # default multiplier
            next_multiplier = 8
            if hour_taken == 1:
                
                if previous_hour_free:
                    now_multiplier , next_multiplier = select_multiplier_depending_if_previous_hour_free(index)
                    shade += ("|" * now_multiplier)
                    previous_hour_free= not previous_hour_free

                else:

                    if index == mappings["7 to 8"] or index == mappings["9 to 10"] :
                        shade += "|" * 9
                    else:
                        shade += "|" * next_multiplier
            else:
                shade+="\t"
                previous_hour_free= True 




        else:

            if hour_taken == 1:
                
                if previous_hour_free:
                    now_multiplier , next_multiplier = select_multiplier_depending_if_previous_hour_free(index)
                    shade += ("|" * now_multiplier)
                    previous_hour_free= not previous_hour_free
                                                                             
                else:
                    shade += "|" * next_multiplier
            else:
                shade+="\t"
                previous_hour_free= True 


    print(tabs_before_printing_day_to_screen+ shade)
    print(tabs_before_printing_day_to_screen+ shade)
    print(tabs_before_printing_day_to_screen+ shade)
    print(tabs_before_printing_day_to_screen+ shade)



# used to ensure a consistent shading of the timetable
def select_multiplier_depending_if_previous_hour_free(index):

    if index == mappings["8 to 9"]:
        now_multiplier = 9
        next_multiplier = 9
        return ( now_multiplier, next_multiplier)

    elif index == mappings["9 to 10"]:
        now_multiplier = 10
        next_multiplier = 8
        return ( now_multiplier, next_multiplier)
    else:
        now_multiplier = 10
        next_multiplier = 8
        return ( now_multiplier, next_multiplier)


int_to_days_of_week ={
    0 : "Mon",
    1 : "Tue",
    2 : "Wed",
    3 : "Thu",
    4 : "Fri",
        
}


# take in a timetable of the whole week and 
# first split it each day's schedule to one hour periods
# map each of those slots to the array that represents that an hour is taken
def map_a_whole_timetable_into_one_hour_slots_and_print(timetable):
    print_hour_string_before_timetable()

    for day in range(5):
        list_of_one_hour_slots = split_into_one_hour_components(timetable.array_of_week_schedule[day])
        map_one_hour_slots_to_hour_taken_array( list_of_one_hour_slots, array_of_one_hour_slots_of_week[day])
        print(int_to_days_of_week[day], end= "")
        print_a_timetable_to_the_terminal( array_of_one_hour_slots_of_week[day])
    
map_a_whole_timetable_into_one_hour_slots_and_print(timetable2)
print_once = True
map_a_whole_timetable_into_one_hour_slots_and_print(timetable1)
