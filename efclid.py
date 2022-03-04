a, b = int(input('Введите число a: ')), int(input('Введите число b: '))
print('Решаю...')
while b:
    a, b = b, a % b
print('НОД:', a)
