def has_digit(password):
    return any(char.isdigit() for char in password)


def is_very_long(password):
    return len(password) > 12


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isalnum() for char in password)


if __name__ == '__main__':
    password = input("Введите пароль: ")

    checks = [
        has_digit,
        is_very_long,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]

    score = 0
    for check in checks:
        if check(password):
            score += 2
    print(f"рейтинг пароля = {score}")
