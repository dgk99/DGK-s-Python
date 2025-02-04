import struct

bar = 1024
foo = 3.18

foo_byte = struct.pack('f', foo)
print(f"[foo_byte] : {foo_byte}")

print(f"[bar] : {bar}, [data type of bar] : {type(bar)}")

bar_byte = bar.to_bytes(4, 'big')

print(f"[bar] : {bar_byte}, [data type of bar] : {type(bar_byte)}")
# 현재 값을 byte 값으로 표현