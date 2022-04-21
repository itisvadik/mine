number = 16**23 + 4**12 - 32**6
str_number = ''
while number > 0:
    ost = number % 4
    str_number += str(ost)
    number //= 4
print(str_number[::-1])
for i in range(4):
    print(str_number.count((str(i))))
