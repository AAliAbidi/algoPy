#R-1.2 Write a short Python function, is even(k), that takes an integer value and
#returns True if k is even, and False otherwise. However, your function
#cannot use the multiplication, modulo, or division operators.

def even(num):
    if (num&1) == 0:
        print(bool(True))
    else:
        print(bool(False))
even(3)
