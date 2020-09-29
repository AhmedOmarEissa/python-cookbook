#Start With , End With
filename = 'spam.txt'
filename.endswith('.txt')
filename.startswith('file:') 
url = 'http://www.python.org' 
url.startswith('http:')


#fnmatch
from fnmatch import fnmatch, fnmatchcase 
fnmatch('foo.txt', '*.txt')


#stripping 

 # Character stripping 
t = '-----hello=====' 
t.lstrip('-') 
t.strip('-=') 