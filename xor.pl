#!/usr/bin/perl
use strict;

scalar(@ARGV) >= 2 or die "usage: $0 cipher_file key [repeat_size] > xored_file";
my $repeat = $ARGV[2];

my @files;
foreach my $i (0, 1)
{
    open(FILE, "<$ARGV[$i]") or die $!;
    binmode FILE;
    while (<FILE>) { $files[$i] .= $_ }
    close FILE;
}

my $i = 0;
my @clear;
while (1)
{
    my $cipher_byte = substr($files[0], $i, 1);
    my $key_byte    = substr($files[1], ($repeat ? $i % $repeat : $i), 1);

    length($cipher_byte) or last; # end of file

    if (!length($key_byte))
    {
        $repeat or last; # end of key

        # previous pixel color value
        push @clear, $clear[$i-3];
    }
    else
    {
        # print XORed
        push @clear, chr(ord($cipher_byte)^ord($key_byte));
    }

    $i++;
}

print join('', @clear);
