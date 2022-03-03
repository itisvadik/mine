n = int(input('Введите число: '))
a = [i for i in range(1, n+1)]
print(a)
m = a[0]
for i in range(n):
    if a[i] > m:
        m = a[i]
print('Самое большое число: ', m)
