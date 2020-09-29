# Example of iterating over two sequences as one

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

for x, y in zip(a, b):
    print(x,y)


from itertools import zip_longest
for i in zip_longest(a,b): 
    print(i)


for i in zip_longest(a,b,fillvalue=0): 
    print(i)

