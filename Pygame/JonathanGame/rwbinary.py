import struct

with open("binary.bat", "wb") as file:
    for n in range(1000):
        data = struct.pack("i", n)
        file.write(data)

with open("binary.bat", "rb") as file:
    size = struct.calcsize("i")
    bytes_read = file.read(size)
    while bytes_read:
        value = struct.unpack("i", bytes_read)
        value = value[0]
        print(value, end=" ")
        bytes_read = file.read(size)




