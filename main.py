from unit_1 import (find_longest_name,
                    sum_of_name_lengths, print_shortest_names,
                    create_name_length_file, print_names_by_length)


def main():
    filename = 'names.txt'
    #    longest_name = find_longest_name(filename)
    #    print(longest_name)
    #    sum_of_name_lengths(filename)
    # קריאה לפונקציה עם שם הקובץ 'names.txt'
    # print_shortest_names('names.txt')
    # input_filename = 'names.txt'
    # output_filename = 'name_length.txt'
    # create_name_length_file(input_filename, output_filename)
    length = int(input("Enter name length: "))
    print_names_by_length(length, filename)

if __name__ == "__main__":
    main()
