# Example of iterating over lines of a file with an extra lineno attribute
def parse_data(filename):
    with open(filename, 'rt') as f:
         for lineno, line in enumerate(f, 1):
             fields = line.split()
             try:
                 count = int(fields[1])
             except ValueError as e:
                 print('Line {}: Parse error: {}'.format(lineno, e)) #show error logs

parse_data('10.iterate_over_the_index-value_pairs_of_a_list/sample.dat')

