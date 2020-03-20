from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation,
)

def get_char_type(char: str):
    if char in ascii_lowercase:
        return ascii_lowercase

    if char in ascii_uppercase:
        return ascii_uppercase

    if char in digits:
        return digits

    raise ValueError
