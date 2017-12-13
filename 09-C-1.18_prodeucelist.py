# C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

###################
#Logic for looping
#i = 0
#i = 0 +1
#i* i =  0

#i = 1
#i = 1+1
#i * i = 2

#i = 2
#i = 2+1
#i * i = 6
##################
def fun():
    ary=[]
    j = 0
    for i in range(0, 10):
        j = i
        i = i+1
        ary.append(j*i)
    print (ary)
fun()