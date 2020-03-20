#!/usr/bin/python
# from modules.caeser_cipher import encrypt, decrypt
import sys, getopt

def main(argv):
    # TODO: GET THE ARGS AND OPTIONS RIGHT
    # https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    print(argv)
    opts, args = getopt.getopt(argv, "hc:o")
    print(opts)
    print(args)

if __name__ == '__main__':
    main(sys.argv[1:])
