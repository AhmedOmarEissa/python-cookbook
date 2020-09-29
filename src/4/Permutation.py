items = ['a', 'b', 'c']
from itertools import permutations 
for p in permutations(items):
    print(p);

from itertools import combinations 
for c in combinations(items,3):
    print(c);

