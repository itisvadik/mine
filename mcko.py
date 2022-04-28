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

task3()
