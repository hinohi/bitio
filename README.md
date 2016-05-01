# bitio

Input/output utirites of bit basis file

## How to use

```py
from bitio import bit_open

f = bit_open(file_name, "r")
x = f.read()           # return 1 or 0
x = f.read_bits(count) # return int

f = bit_open(file_name, "w")
f.write(bit)              # write 1 if bit else 0
f.write_bits(bits, count) # write 'count bits'
f.close()
```

These are same

```py
f.write_bits(bits, count)

for i in range(count-1, -1, -1):
  if bits & (1 << i):
    f.write(1)
  else:
    f.write(0)
```

othe interface

```py
l = []
wrapper = ByteWrapper(l.append)
f = bit_wrap(wrapper, "w")
f.write_bits(0b110000101, 10)
print l # ["a"]
f.close()
print l # ["a", "@"]
```
