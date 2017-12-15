# C-1.20 Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible
# order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.

import random
def function (size):
    l = [0]*size
    for i in range(size):
        l[i] = int(input("Enter %d element: "%i))
    print("\n")
    print("List is: \n", l)
    random.shuffle(l)
    print("\nRandom number betwwen 1 to 100")
    print(random.randint(10, 100))    # Print any random number between 10 to 100 using randint(a, b)
    print("\nList after shuffeling: ")
    print(l)                         # Print shuffel element of "l" list
size = int(input("Enter range: "))
function(size)