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

# write 'count' bits using write_bits
f.write_bits(bits, count)

# write 'count' bits using write
for i in range(count-1, -1, -1):
    if bits & (1 << i):
        f.write(1)
    else:
        f.write(0)
"""


from .bit_file import BitFileReader, BitFileWriter


VERSION = (0, 1, 1)


def bit_open(name, mode="r"):
    """\
mode: "r" -> read mode
      "w" -> write mode
"""
    if mode in ["w", "wb"]:
        return BitFileWriter(name)
    elif mode in ["r", "rb"]:
        return BitFileReader(name)
    else:
        raise ValueError("Invalid bit-file mode '%s'"%(mode))