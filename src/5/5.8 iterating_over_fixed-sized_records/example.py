# Example of iterating of fixed-size records
#
# The file 'data.bin' contains 32-byte fixed size records
# that consist of a 4-digit number followed by a 28-byte string.

from functools import partial
RECORD_SIZE = 32
path ='5.8 iterating_over_fixed-sized_records/'

with open(path + 'data.bin', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)
        print('----')

