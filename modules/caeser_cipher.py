from modules.string_type import get_char_type
from string import punctuation

def cipher(message: str, key: int):
    output = ''

    for letter in message:
        if letter in punctuation or letter == ' ':
            output += letter
            continue

        char_list = get_char_type(letter)
        char_index = (char_list.index(letter) + key) % len(char_list)

        output += char_list[char_index]

    return output

def encrypt(message: str, key: int):
    return cipher(message, key)


def decrypt(message: str, key: int):
    return cipher(message, -key)
