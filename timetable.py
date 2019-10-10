# each day, classes run from 7am - 7pm, that is 12 hours
# this is the total time allocated for classes for the whole week, classes may fall anywhere in between 7am -7pm , Monday to Friday
monday = [ 'monday(7-8)', 'monday(8-9)', 'monday(9-10)', 'monday(10-11)', 'monday(11-12)', 'monday(12-1)', 'monday(1-2)', 'monday(2-3)', 'monday(3-4)', 'monday(4-5)', 'monday(5-6)', 'monday(6-7)' ]
tuesday = [ 'tuesday(7-8)', 'tuesday(8-9)', 'tuesday(9-10)', 'tuesday(10-11)', 'tuesday(11-12)', 'tuesday(12-1)', 'tuesday(1-2)', 'tuesday(2-3)', 'tuesday(3-4)', 'tuesday(4-5)', 'tuesday(5-6)', 'tuesday(6-7)' ]
wednesday = [ 'wednesday(7-8)', 'wednesday(8-9)', 'wednesday(9-10)', 'wednesday(10-11)', 'wednesday(11-12)', 'wednesday(12-1)', 'wednesday(1-2)', 'wednesday(2-3)', 'wednesday(3-4)', 'wednesday(4-5)', 'wednesday(5-6)', 'wednesday(6-7)' ]
thursday = [ 'thursday(7-8)', 'thursday(8-9)', 'thursday(9-10)', 'thursday(10-11)', 'thursday(11-12)', 'thursday(12-1)', 'thursday(1-2)', 'thursday(2-3)', 'thursday(3-4)', 'thursday(4-5)', 'thursday(5-6)', 'thursday(6-7)' ]
friday = [ 'friday(7-8)', 'friday(8-9)', 'friday(9-10)', 'friday(10-11)', 'friday(11-12)', 'friday(12-1)', 'friday(1-2)', 'friday(2-3)', 'friday(3-4)', 'friday(4-5)', 'friday(5-6)', 'friday(6-7)' ]

#let's store the total time for the whole week into one list
# I'm using this method to avoid making the list hashed (a hashed list or dictionary is quite hard to remove duplicate items from them)
total_number_of_hours_per_week = []
for i in monday:
    total_number_of_hours_per_week.append(i)
for i in tuesday:
    total_number_of_hours_per_week.append(i)
for i in wednesday:
    total_number_of_hours_per_week.append(i)
for i in thursday:
    total_number_of_hours_per_week.append(i)
for i in friday:
    total_number_of_hours_per_week.append(i)

# ==================== THIS IS WHERE YOU ADD A TIMETABLE (for the whole week) ====================
# timetable one classes for the whole week
timetable_one = [ 'monday(7-8)', 'monday(8-9)', 'monday(11-12)','tuesday(11-12)', 'tuesday(12-1)', 'wednesday(7-8)', 'wednesday(8-9)', 'wednesday(9-10)', 'wednesday(10-11)', 'friday(12-1)', 'friday(1-2)', 'friday(2-3)' ]
# timetable two classes for the whole week
timetable_two = [ 'monday(4-5)','tuesday(7-8)', 'tuesday(8-9)','tuesday(2-3)', 'wednesday(9-10)', 'wednesday(10-11)', 'wednesday(4-5)', 'thursday(7-8)', 'thursday(8-9)','thursday(2-3)', 'thursday(3-4)','friday(12-1)'  ]
# add your timetable here e.g 'timetabel_three'

# okay, let's find free hours that are common in each time table
# firstly let's append the classes for all timetables to total hours per week to create a duplicate of times
for i in timetable_one:
    total_number_of_hours_per_week.append(i)
for i in timetable_two:
    total_number_of_hours_per_week.append(i)
# remember that duplicate times are occupied times, this means that there are classes running at this time
# now, let's remove duplicate times from out total time to remain with free times
none_dupes = list(dict.fromkeys(total_number_of_hours_per_week))

#free hours that are common to each timetable
common_free_hours = none_dupes
print(common_free_hours)

