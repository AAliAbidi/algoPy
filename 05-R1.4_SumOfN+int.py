#R-1.4 Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the positive integers smaller than n.

def function():
    square=[]
    sum = 0
    num = int(input("Enter Positive integer: "))
    if(num < 0):
         print("Program not accepting %d value, Program going to QUIT!"%num)
    else:
        for i in range(0, num):
            square.append(i*i)
            sum  += i*i
        print(square)
        print("Sum of elements is: \n", sum)
function()