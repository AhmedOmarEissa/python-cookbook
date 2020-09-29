import os
#Get the last component of the path  
path = 'writing_bytes_to_a_text_file/'
os.path.basename(path)
os.path.dirname(path)

os.path.exists('writing_bytes_to_a_text_file/')
os.path.isdir('writing_bytes_to_a_text_file/')
os.path.isfile('writing_bytes_to_a_text_file/example.py')

os.listdir()

[name for name in os.listdir() if os.path.isfile(os.path.join( name))] #get all files in a director

[name for name in os.listdir() if name.endswith('.py')]

import glob
glob.glob('*.py')
from fnmatch import fnmatch
[name for name in os.listdir() if fnmatch(name, '*.py')]