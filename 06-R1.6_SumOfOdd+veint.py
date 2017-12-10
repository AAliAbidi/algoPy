#R-1.6 Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the odd positive integers smaller than n.
def sumofodd():
    num = int(input("Enter positive integer: "))
    sum = 0
    array = []
    squareArray = []
    if num < 0:
        print("Enter positive integer value, Program QUIT!")
    else:
        for i in range(1, num):
            if (i%2) != 0:
                array.append(i)
                squareArray.append(i*i)
                sum += i*i
        print(array)
        print(squareArray)
        print("Sum is :\n", sum) 
sumofodd()