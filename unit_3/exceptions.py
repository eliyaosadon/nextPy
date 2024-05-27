class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, position):
        self.char = char
        self.position = position
        super().__init__(f"The username contains an illegal character '{char}' at position {position}")


class UsernameTooShort(Exception):
    def __init__(self):
        super().__init__("The username is too short")


class UsernameTooLong(Exception):
    def __init__(self):
        super().__init__("The username is too long")


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
