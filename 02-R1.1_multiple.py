#R-1.1- Write a short Python function, is multiple(n, m), that takes two integer
#values and returns True if n is a multiple of m, that is, n = mi for some
#integer i, and False otherwise.
def multiple(n,m):
    if (n%m) == 0:
       print(bool(True))
    else:
        print(bool(False))
multiple(8,2)
