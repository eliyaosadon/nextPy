def parse_ranges(ranges_string):
    # גנרטור ראשון שמפצל את הטווחים לרשימות של [start, stop]
    def split_ranges(ranges_string):
        for part in ranges_string.split(','):
            yield part.split('-')

    # גנרטור שני שמייצר את המספרים בטווחים
    def generate_numbers(splitted_ranges):
        for start, stop in splitted_ranges:
            start, stop = int(start), int(stop)
            for num in range(start, stop + 1):
                yield num

    # קריאה לגנרטורים
    splitted_ranges = split_ranges(ranges_string)
    return generate_numbers(splitted_ranges)


# בדיקות
print(list(parse_ranges("1-2,4-4,8-10")))  # [1, 2, 4, 8, 9, 10]
print(list(parse_ranges("0-0,4-8,20-21,43-45")))  # [0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45]
