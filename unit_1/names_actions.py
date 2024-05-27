# Ex.1 - finds the longest name in the file
def find_longest_name(filename):
    with open(filename) as f: return max(f.read().splitlines(), key=len)


# Ex.2 - prints the sum of all the names in the file
def sum_of_name_lengths(filename):
    with open(filename) as f:
        print(sum(len(name) for name in f.read().splitlines()))


# Ex.3 - prints the shortest names in the file
def print_shortest_names(filename):
    with open(filename) as f: names = f.read().splitlines()
    min_length = min(map(len, names))
    print('\n'.join(name for name in names if len(name) == min_length))


# Ex.4 - creates new file that includes all the names lengths in the original file
def create_name_length_file(input_filename, output_filename):
    with open(input_filename) as f_in, open(output_filename, 'w') as f_out:
        f_out.write('\n'.join(str(len(name.strip())) for name in f_in))


# Ex.5 - asks for a number and presents all the names that their length equals to the input number
def print_names_by_length(length, filename):
    with open(filename) as f:
        names = [name.strip() for name in f if len(name.strip()) == length]
        print('\n'.join(names))
