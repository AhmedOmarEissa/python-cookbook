# Some examples of reading text files with different options
#
# The file sample.txt is a UTF-8 encoded text file with Windows
# line-endings (\r\n).

# (a) Reading a basic text file (UTF-8 default encoding)
path ='reading_and_writing_text_data/'
print("Reading a simple text file (UTF-8)")
with open(path  +'sample.txt', 'rt') as f:
    for line in f:
        print(repr(line));

# (b) Reading a text file with universal newlines turned off
print("Reading text file with universal newlines off")
with open(path +'sample.txt', 'rt', newline='') as f:
    for line in f:
        print(repr(line))

# (c) Reading text file as ASCII with replacement error handling
print("Reading text as ASCII with replacement error handling")
with open(path +'sample.txt', 'rt', encoding='ascii', errors='replace') as f:
    for line in f:
        print(repr(line))

# (d) Reading text file as ASCII with ignore error handling
print("Reading text as ASCII with ignore error handling")
with open(path +'sample.txt', 'rt', encoding='ascii', errors='ignore') as f:
    for line in f:
        print(repr(line))

