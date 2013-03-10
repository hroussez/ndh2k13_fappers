#!/usr/bin/python

import sys
from hashlib import sha512
from random import seed, choice
from struct import pack
from os import stat

filename = 'dafuq.bmp'

cipher_fh = open(filename)
cipher = cipher_fh.read()

filestat = stat(filename)
expected_header = pack('<2sI', "BM", filestat.st_size)

passwords = open('passwords.txt')


def check():
    for i in range(5):
        if choice(range(0,256)) != ord(cipher[i])^ord(expected_header[i]):
            return
        if i == 4:
            print "%s seems valid" % line

for line in passwords:
    line = line.rstrip()
    seed(sha512(line.rstrip()).digest())
    check()
