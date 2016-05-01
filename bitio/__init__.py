# -*- coding: utf-8 -*-
#
# bitio/bit_file.py
#
"""\
Input/output utirites of a bit-basis file.

------------------------------------------
how to use:

from bitio import bit_open, bit_wrap, ByteWrapper

f = bit_open(file_name, "r")
f.read()           # return 1 or 0
f.read_bits(count) # return int

f = bit_open(file_name, "w")
f.write(bit)              # write 1 if bit else 0
f.write_bits(bits, count) # write 'count bits'
f.close()

l = []
wrapper = ByteWrapper(l.append)
f = bit_wrap(wrapper, "w")
f.write_bits(0b110000101, 10)
print l # ["a"]
f.close()
print l # ["a", "@"]
"""


from .bit_file import BitFileReader, BitFileWriter
from .byte_wrapper import ByteWrapper

VERSION = (0, 2, 0)


def bit_open(name, mode="r"):
    """\
name: file name
mode: "r" -> read mode
      "w" -> write mode
"""
    if mode in ["w", "wb"]:
        return BitFileWriter(name)
    elif mode in ["r", "rb"]:
        return BitFileReader(name)
    else:
        raise ValueError("Invalid bit-file mode '%s'"%(mode))

def bit_wrap(byte_file, mode="r"):
    """\
byte_file: byte basis file-like object
mode: "r" -> read mode
      "w" -> write mode
"""
    if mode in ["w", "wb"]:
        return BitFileWriter.from_file(byte_file)
    elif mode in ["r", "rb"]:
        return BitFileReader.from_file(byte_file)
    else:
        raise ValueError("Invalid bit-file mode '%s'"%(mode))



