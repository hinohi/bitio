# -*- coding: utf-8 -*-
#
# test.py
#
import unittest
import os

import bitio

class TestWiter(unittest.TestCase):

    def setUp(self):
        self.test_file_name = ".test"

    def _test(self):
        f = open(self.test_file_name, "rb")
        self.assertEqual(ord(f.read(1)), 0b01100110)
        self.assertEqual(ord(f.read(1)), 0b10000000)
        f.close()
        os.remove(self.test_file_name)

    def test_with(self):
        with bitio.BitFileWriter(self.test_file_name) as f:
            for i in ([0, 1, 1, 0]*2 + [1]):
                f.write(i)
        self._test()

    def test_write(self):
        f = bitio.BitFileWriter(self.test_file_name)
        for i in ([0, 1, 1, 0]*2 + [1]):
            f.write(i)
        f.close()
        self._test()

    def test_write_bits(self):
        f = bitio.BitFileWriter(self.test_file_name)
        f.write_bits(0b011001101, 9)
        f.close()
        self._test()

class TestReader(unittest.TestCase):

    def setUp(self):
        self.test_file_name = ".test"
        with bitio.BitFileWriter(self.test_file_name) as f:
            for i in ([0, 1, 1, 0]*2 + [1]):
                f.write(i)

    def test_with(self):
        with bitio.BitFileReader(self.test_file_name) as f:
            for i in ([0, 1, 1, 0]*2 + [1] + [0]*7):
                self.assertEqual(f.read(), i)
            self.assertRaises(IOError, f.read)

    def test_read(self):
        f = bitio.BitFileReader(self.test_file_name)
        for i in ([0, 1, 1, 0]*2 + [1] + [0]*7):
            self.assertEqual(f.read(), i)
        self.assertRaises(IOError, f.read)
        f.close()

    def test_read_bits(self):
        f = bitio.BitFileReader(self.test_file_name)
        self.assertEqual(f.read_bits(9), 0b011001101)
        self.assertEqual(f.read_bits(7), 0)
        self.assertRaises(IOError, f.read_bits, 1)
        f.close()

    def test_empty(self):
        emp_file = "emp"
        open(emp_file, "wb").close()
        f = bitio.BitFileReader(emp_file)
        self.assertRaises(IOError, f.read)
        f.close()
        os.remove(emp_file)

if __name__ == '__main__':
    unittest.main()