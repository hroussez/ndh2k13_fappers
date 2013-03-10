#!/usr/bin/perl

scalar(@ARGV) ne 3 and die "usage $0 <encrypted> <width> <height>";
print
     "\x42\x4d"             # Magic number
    .pack("i", -s $ARGV[0]) # Size of the BMP file
    ."\x00\x00\x00\x00"     # Application specific
    ."\x36\x00"             # Offset of the 1st pixel array
    ."\x28\x00\x00\x00"     # Size of DIB header
    ."\x80\x04\x00\x00"     # Width of the bitmap
    ."\x60\x03\x00\x00"     # Height of the bitmap
    ."\x01\x00"             # Number of color planes
    ."\x18\x00"             # Number of bits per pixel
    ."\x00\x00\x00\x00"     # BI_RGB, no pixel array compression used
    ."\x10\x00\x00\x00"     # Size of the raw data in the pixel array
    .pack("i", $ARGV[1])    # Horizontal resolution
    .pack("i", $ARGC[2])    # Vertical resolution
    ."\x00\x00\x00\x00"     # Number of colors in the palette
    ."\x00\x00\x00\x00";    # 0 means all colors are important
