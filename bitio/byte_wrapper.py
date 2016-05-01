# -*- coding: utf-8 -*-
#
# bitio/byte_wrapper.py
#
class ByteWrapper(object):
    def __init__(self, callable_object):
        if not callable(callable_object):
            raise TypeError("must be allable object")
        self.callable_object = callable_object

    def read(self, count=1):
        try:
            s = self.callable_object()
        except:
            s = ""
        return s

    def write(self, byte):
        self.callable_object(byte)

