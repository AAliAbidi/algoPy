#R-1.3 Write a short Python function, minmax(data), that takes a sequence of
#one or more numbers, and returns the smallest and largest numbers, in the
#form of a tuple of length two. Do not use the built-in functions min or
#max in implementing your solution.

def minmax (size):
    l = [0]*size
    for i in range(size):
        l[i] = int(input("Enter NUmber: "))
    print("list is \n", l)
    min = l[0]
    max = l[0]
    for k in range(0, size-1):
        if(l[k+1]>max):
            max = l[k+1]
        if(l[k+1]<min):
            min = l[k+1]
    tup = (min, max)
    print(tup)
minmax(5)