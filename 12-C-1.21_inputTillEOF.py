# C-1.21 Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).
import sys
#var = input("enter string : >")
while 1:
    try:
        var = sys.stdin.readline()
        print("Enter line")
        print("^^^^^^^^^^\n")
    except EOFError:
        break
    except:
        exit()
print(var[::-1])
