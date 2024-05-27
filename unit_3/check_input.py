import string

from unit_3.exceptions import PasswordMissingUppercase, PasswordMissingLowercase, PasswordMissingDigit, \
    PasswordMissingSpecial, PasswordTooLong, PasswordTooShort, UsernameTooShort, UsernameTooLong, \
    UsernameContainsIllegalCharacter


def check_input(username, password):
    # Check username validity
    if not (3 <= len(username) <= 16):
        if len(username) < 3:
            raise UsernameTooShort()
        else:
            raise UsernameTooLong()
    for i, char in enumerate(username):
        if char not in string.ascii_letters + string.digits + "_":
            raise UsernameContainsIllegalCharacter(char, i)

    # Check password validity
    if not (8 <= len(password) <= 40):
        if len(password) < 8:
            raise PasswordTooShort()
        else:
            raise PasswordTooLong()

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if not has_upper:
        raise PasswordMissingUppercase()
    if not has_lower:
        raise PasswordMissingLowercase()
    if not has_digit:
        raise PasswordMissingDigit()
    if not has_special:
        raise PasswordMissingSpecial()

    print("OK")


def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            check_input(username, password)
            break
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
