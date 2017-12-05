# Page No.3 Calculate GPA Example
print("Welcome to GPA calculator.")
print("Please enter all your letter grades, one per line.")
print("Enter blank line to designate at end.")
POINTS = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67, 'C+':2.33, 
'C':2.0, 'C-':1.67, 'D+':1.33, 'D':1.0, 'F':0.0}
NUM_COURSES = 0
TOTAL_POINTS = 0
DONE = False
while not DONE:
    GRADE = input()
    if GRADE == ' ':
        DONE = True
    elif GRADE not in POINTS:
        print("Unkown grade '{0}' being ignored".format(GRADE))
    else:
        NUM_COURSES +=1
        TOTAL_POINTS += POINTS[GRADE]
if NUM_COURSES > 0:
    print('Your GPA is {0:3}'.format(TOTAL_POINTS/NUM_COURSES))