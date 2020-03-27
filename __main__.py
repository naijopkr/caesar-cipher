#!/usr/bin/python
from caesar_cipher import encrypt, decrypt
from unidecode import unidecode
import sys, getopt


def help():
    print('caesar-cipher -i <inputfile> -o <outputfile> -k <key> [-d]')
    print()
    print('\t-d\tdecrypt message')
    print('\t-k\tkey for encryt/decrypt')
    print('\t-i\tpath to input file')
    print('\t-o\tpath to output file')
    print()

def main(argv):
    input_file = ''
    output_file = 'output.txt'
    key = 0
    is_decrypt = '-d' in argv
    try:
        opts, _args = getopt.getopt(argv, "dhi:k:o:")
    except getopt.GetoptError:
        help()

    for opt, arg in opts:
        if opt == '-h':
            help()
        elif opt == '-i':
            input_file = arg
        elif opt == '-o':
            output_file = arg
        elif opt == '-k':
            key = int(arg)

    if input_file:
        file_to_process = open(input_file, '+r')
        file_str = unidecode(file_to_process.read())

        if (is_decrypt):
            message = decrypt(file_str, key)
        else:
            message = encrypt(file_str, key)

        output = open(output_file, '+w')
        output.write(message)

if __name__ == '__main__':
    main(sys.argv[1:])
