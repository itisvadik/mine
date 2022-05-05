def task1():
    s = '7' * 1000 + '3' * 1000
    while '777' in s or '333' in s:
        s = s.replace('777', '3', 1)
        s = s.replace('333', '7', 1)
    print(s)


def task2():
    print('x y z w F')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    F = (x <= y) and (y <= w) and (z <= x)
                    if F:
                        print(x, y, z, w, F)


def task3():
    for i in range(1, 1000):
        n = i
        bin_n = bin(n)[2:]
        bin_n += bin_n[-1] * 2
        if bin_n.count('1') % 2 == 0:
            bin_n += '0'
        else:
            bin_n += '1'
        r = int(bin_n, 2)
        if r > 84:
            print(i)
            break


def task5():
    T = [0, 0, 1, 1, 1]
    for i in range(5, 11):
        T.append(T[i - 1])
        if i % 4 == 0:
            T[i] += T[i//4]
    print(T)
    for i in range(11, 80):
        if i == 30:
            T.append(0)
        elif i >= 40:
            T.append(T[i - 1] + (T[i // 4] if not i % 4 else 0))
        else:
            T.append(T[i - 1])
    print(T)


def task6():
    for A in range(1, 100):
        flag = True
        for x in range(1, 10000):
            if ((x % 25 != 0 or x % 60 != 0) <= (x % A != 0)) == 0:
                flag = False
                break


task6()
