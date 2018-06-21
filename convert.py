#!/usr/bin/python3

import sys
import binascii

filename = sys.argv[1]

with open(filename, 'rb') as input_file:
    word = input_file.read(1)
    while word:
        output = binascii.hexlify(word)
        print("0X%s, " % output.decode('utf-8'), end='')
        word = input_file.read(1)
