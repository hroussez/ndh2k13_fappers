#!/usr/bin/python

"""

*`'\{            Turk1sh H4ck3rs - BMP encryption tool           }/'`*

-- because that's the only way to share pr0n without being caught !

Usage: encrypt.py [bmp] [pwd]

-> this will produce dafuq.bmp, ready to share !




======================================================================
      Help us spread great pr0n picz & vidz around Turkish web !

                          Fappers gonna fap !
======================================================================


"""

import sys
from hashlib import sha512
from struct import pack, unpack
from random import seed, choice

class BadBmpError(Exception):
    def __init__(self):
        Exception.__init__(self)

class BmpNot24bppError(Exception):
    def __init__(self):
        Exception.__init__(self)

class BitmapFile:
    """
    Bitmap file handling class
    """
    
    BMP_SIGN = 0
    BMP_SIZE = 1
    BMP_RES1 = 2
    BMP_RES2 = 3
    BMP_DATA = 4

    DIB_HSIZ = 0
    DIB_WDTH = 1
    DIB_HGHT = 2
    DIB_PLAN = 3
    DIB_NBPP = 4
    DIB_COMP = 5
    DIB_SIZE = 6
    DIB_HRES = 7
    DIB_VRES = 8
    DIB_COLR = 9
    DIB_ICLR = 10


    def __init__(self, bmp=None):
        self._bmp = bmp
        # try to open file
        self._f = open(self._bmp, 'rb')

        # init structures
        self._bmp_header = None
        self._dib_header = None

        # load file (and perform some other checks too)
        self._read_bmp_header()
        self._read_dib_header()

    def _read(self, size):
        return self._f.read(size)

    def _read_uint32(self):
        return unpack('<I', self._f.read(4))[0]

    def _read_uint16(self):
        return unpack('<H', self._f.read(2))[0]

    def _read_bmp_header(self):
        self._bmp_header = unpack('<2sIHHI', self._read(14))
        if self._bmp_header[self.BMP_SIGN] != 'BM':
            raise BadBmpError()
        return

    def _read_dib_header(self):
        self._dib_header = unpack('<IIIHHIIIIII', self._read(40))
        if self._dib_header[self.DIB_NBPP] != 24:
            raise BmpNot24bppError()
        return

    def encrypt(self, key):
        # derive key
        h = sha512(key).digest()
        seed(h)
        keystream = []
        for i in range(337):
            keystream.append(choice(range(0,256)))
        string = ''.join([chr(c) for c in keystream]).encode('hex')
        step = 4
        for i in range(0, len(string), 4):
            print string[i:step],
            step += 4


        # encrypt content with our keystream
        self._f.seek(0, 0)
        content = self._f.read()
        output = []
        for i in range(len(content)):
            output.append(chr(ord(content[i])^keystream[i%337]))
        open('dafuq.bmp','wb').write(''.join(output))
        print "[i] C'mon, spread it around now !"


if __name__ == '__main__':
    if len(sys.argv)==3:
        bmp = BitmapFile(sys.argv[1])
        bmp.encrypt(sys.argv[2])
