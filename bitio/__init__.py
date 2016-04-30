# -*- coding: utf-8 -*-
#
# bitio/bit_file.py
#
"""\
Input/output utirites of a bit-basis file.


how to use:

from bitio import bit_open

f = bit_open(file_name, "r")
f.read()           # return 1 or 0
f.read_bits(count) # return int

f = bit_open(file_name, "w")
f.write(bit)              # write 1 if bit else 0
f.write_bits(bits, count) # write 'count bits'
f.close()


these are same:

f.write_bits(bits, count)

for i in range(count-1, -1, -1):
    if bits & (1 << i):
        f.write(1)
    else:
        f.write(0)
"""


from .bit_file import bit_open, BitFileReader, BitFileWriter

VERSION = (0, 1, 1)
