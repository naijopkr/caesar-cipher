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

def encrypt(message: str, key: int):

    output = ''
    for letter in message:
        if letter in punctuation or letter == ' ':
            output += letter
            continue

        char_list = get_char_type(letter)
        char_index = (char_list.index(letter) + key) % len(char_list)

        output += char_list[char_index]

    print(output)

if __name__ == '__main__':
    message = input('Insert the message to be encrypted: ')
    key = int(input('Insert the key: '))
    encrypt(message, key)
