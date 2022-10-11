BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 100
lines = 50
chars = 25

total_chars =  pages * lines * chars
total_bytes = total_chars * BYTES_ONE_CHAR
a = 1024 * BYTES_ONE_CHAR
b = 1024 * a
c = 1.44 * b
disk_size = c

print(c // total_bytes)
