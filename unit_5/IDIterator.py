
def check_id_valid(id_number):
    id_str = str(id_number).zfill(9)
    total = 0
    for i, digit in enumerate(id_str):
        num = int(digit) * (1 if i % 2 == 0 else 2)
        if num > 9:
            num = num // 10 + num % 10
        total += num
    return total % 10 == 0

# בדיקת הפונקציה
# print(check_id_valid(123456780))  # False
# print(check_id_valid(123456782))  # True


class IDIterator:
    def __init__(self, id_):
        self.id_ = id_

    def __iter__(self):
        return self

    def __next__(self):
        while self.id_ < 999999999:
            self.id_ += 1
            if check_id_valid(self.id_):
                return self.id_
        raise StopIteration


# בדיקת המחלקה
# id_iter = IDIterator(123456780)
# for _ in range(10):
#    print(next(id_iter))


def id_generator(id_):
    current_id = id_
    while current_id < 999999999:
        current_id += 1
        if check_id_valid(current_id):
            yield current_id


# בדיקת פונקציית הגנרטור
# gen = id_generator(123456780)
# for _ in range(10):
#    print(next(gen))


def main():
    id_input = int(input("Enter ID: ").strip())
    choice = input("Generator or Iterator? (gen/it)? ").strip().lower()

    if choice == "it":
        id_iter = IDIterator(id_input)
        for _ in range(10):
            print(next(id_iter))
    elif choice == "gen":
        id_gen = id_generator(id_input)
        for _ in range(10):
            print(next(id_gen))
    else:
        print("Invalid choice. Please enter 'gen' or 'it'.")


if __name__ == "__main__":
    main()
