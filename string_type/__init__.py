from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation,
)
import re

def get_char_type(char: str):
    if re.search(char, ascii_lowercase):
        return ascii_lowercase

    if re.search(char, ascii_uppercase):
        return ascii_uppercase

    if re.search(char, digits):
        return digits

    raise ValueError
