record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212') 

name, email, *phone_numbers = record  #assign iterable
print(name)
print(phone_numbers)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false' 
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir) 
print(sh) 


#Yeild 
def yfunc():
    for i in [1,2,3]: 
        yield i #yeild create a generator. 

for i in yfunc(): 
    print(i)

#heap 

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23] 
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

heapq.heappop(nums)  #Pop smallest number
heapq.heappush(nums, 10000)


from collections import OrderedDict
d = OrderedDict() 
d['foo'] = 1 
d['bar'] = 2 
d['spam'] = 3 
d['grok'] = 4


a = {}
a['foo'] = 1 
a['bar'] = 2 
a['spam'] = 3 
a['grok'] = 4

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

[*zip(prices.values(), prices.keys())]


#lambda function 

a = [ 
    {'x': 2, 'y': 3},
    {'x': 1, 'y': 4},
    {'x': 2, 'y': 3},
    {'x': 2, 'y': 3},
    {'x': 10, 'y': 15}
    ]


x = lambda a: (a['x'],a['y'])
x


#slice

s =slice(1, 6, 2)
[1,2,3,4,5,6][s]

#counter 
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
]
from collections import Counter 
word_counts = Counter(words)
top_three = word_counts.most_common(3) 
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]


#compress
addresses = [
'5412 N CLARK',
'5148 N CLARK', '5800 E 58TH',
'2122 N CLARK'
'5645 N RAVENSWOOD', '1060 W ADDISON', '4801 N BROADWAY', '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
more5
addresses
list(compress(addresses, more5))
['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']