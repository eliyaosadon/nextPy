import string


# חריגות שם משתמש
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, position):
        self.char = char
        self.position = position
        super().__init__(f"The username contains an illegal character '{char}' at index {position}")

    def __str__(self):
        return f"The username contains an illegal character '{self.char}' at index {self.position}"


class UsernameTooShort(Exception):
    def __init__(self):
        super().__init__("The username is too short")


class UsernameTooLong(Exception):
    def __init__(self):
        super().__init__("The username is too long")


# חריגות סיסמה
class PasswordMissingCharacter(Exception):
    def __init__(self):
        super().__init__("The password is missing a character")


class PasswordTooShort(Exception):
    def __init__(self):
        super().__init__("The password is too short")


class PasswordTooLong(Exception):
    def __init__(self):
        super().__init__("The password is too long")


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"{super().__str__()} (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"{super().__str__()} (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"{super().__str__()} (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"{super().__str__()} (Special)"


# פונקציית הבדיקה
def check_input(username, password):
    # בדיקת שם משתמש
    if not (3 <= len(username) <= 16):
        if len(username) < 3:
            raise UsernameTooShort()
        else:
            raise UsernameTooLong()
    for i, char in enumerate(username):
        if char not in string.ascii_letters + string.digits + "_":
            raise UsernameContainsIllegalCharacter(char, i)

    # בדיקת סיסמה
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


# פונקציה ראשית
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
