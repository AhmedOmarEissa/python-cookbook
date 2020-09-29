`#slice iterator
def count(n):
    while n <= 30: 
        yield n
        n += 1
c = count(0)

import itertools
for x in itertools.islice(c, 1, 5):
    print(x)

#skip iterator items

c = count(0)
from itertools import dropwhile

#list(c)
def is_even(x):
    return x %2 == 0

list(dropwhile(is_even , c))

for i in (dropwhile(lambda i: i %2 == 0 , c)): 
    print(i)



x = lambda i: i%2 == 0 
x(8)
