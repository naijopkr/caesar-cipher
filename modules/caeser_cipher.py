# TODO: check the string module docs to solve this
def encrypt(message: str, key: int):
    output = ''
    for letter in message:
        char_code = ord(letter)

        if char_code > 90 or char_code < 0:
            raise ValueError

        if char_code == 32:
            output += chr(char_code)
            continue

        if char_code < 48
            or (char_code > 57 and char_code < 65)
            or (char_code > 90 and char_code < 97):
            char_type = 'symbol'
        elif char_code < 58:
            char_type = 'number'
        elif char_code < 91:
            char_type: 'capital_letter'

        output += chr(32 + (char_code + key) % 91)

    print(output)

if __name__ == '__main__':
    message = input('Insert the message to be encrypted: ')
    key = int(input('Insert the key: '))
    encrypt(message, key)
