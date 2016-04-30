# -*- coding: utf-8 -*-
#
# bit_file.py
#

def bit_open(name, mode="rb"):
    if mode in ["w", "wb"]:
        return BitFileWriter(name)
    elif mode in ["r", "rb"]:
        return BitFileReader(name)
    else:
        raise ValueError("Invalid bit-file mode '%s'"%(mode))

class BaseBitFile(object):
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False
    def __del__(self):
        self.close()

class BitFileReader(BaseBitFile):
    
    def __init__(self, name):
        self.name = name
        self.byte_file = open(name, "rb")
        self.rack = 0
        self.mask = 0x80
    
    def close(self):
        self.byte_file.close()
    
    def _read_byte(self):
        c = self.byte_file.read(1)
        if c == '':
            raise IOError("Bit file is empty!")
        return ord(c)
        
    def read(self):
        if self.mask == 0x80:
            self.rack = self._read_byte()
        ret = 1 if (self.rack & self.mask) else 0
        self.mask >>= 1
        if self.mask == 0:
            self.mask = 0x80
        return ret
    
    def read_bits(self, count):
        if count <= 0:
            return 0
        ret = 0
        mask = 1 << (count - 1)
        while mask > 0:
            if self.mask == 0x80:
                self.rack = self._read_byte()
            if self.rack & self.mask:
                ret |= mask
            self.mask >>= 1
            mask >>= 1
            if self.mask == 0:
                self.mask = 0x80
        return ret


class BitFileWriter(BaseBitFile):
    
    def __init__(self, name):
        self.name = name
        self.byte_file = open(name, "wb")
        self.rack = 0
        self.mask = 0x80
    
    def _flush_byte(self):
        self.byte_file.write(chr(self.rack))
        self.rack = 0
        self.mask = 0x80
        
    def close(self):
        if self.mask != 0x80:
            self._flush_byte()
        self.byte_file.close()
        
    def write(self, bit):
        if bit:
            self.rack |= self.mask
        self.mask >>= 1
        if self.mask == 0:
            self._flush_byte()
    
    def write_bits(self, code, count):
        if count <= 0:
            return
        mask = 1 << (count - 1)
        while mask > 0:
            if code & mask:
                self.rack |= self.mask
            self.mask >>= 1
            mask >>= 1
            if self.mask == 0:
                self._flush_byte()
