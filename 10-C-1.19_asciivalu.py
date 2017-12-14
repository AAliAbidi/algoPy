#C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
#the list [ a , b , c , ..., z ], but without having to type all 26 such
#characters literally.
ary = []
for i in range (97, 123):
    c = chr(i)
    ary.append(c)
print(ary)

