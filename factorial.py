
def fact(n: int) -> int:
    """
    Возвращает факториал от числа n
    """
    if n <= 1:
        return 1
    return fact(n - 1) * n


def gcd(a: int, b: int) -> int:
    """
    Возвращает НОД от чисел a и b, вычесленный по алгоритму Евклида
    """
    return gcd(b, a % b) if b else a


def power(a: float, n: int) -> float:
    """
    Возводит число a в натуральную степень n
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a * a, n // 2)
    # Условие-призрак n % 2 != 0
    return power(a, n-1) * a


def generate_numbers(n: int, m: int, prefix=None) -> None:
    """
    Выводит в консоль все перестановки длинной m в системе счисления n
    """
    if m == 0:
        print(*prefix)
        return
    prefix = prefix or []
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m-1, prefix)
        prefix.pop()


def generate_permutation(n: int, m: int, prefix=None) -> None:
    """
    Выводит в консоль все перестановки длинной m в системе счисления n
    """
    if m > n:
        raise ValueError(f'Длина числа ({m}) не может быть больше основания системы счисления ({n})')
    if m == 0:
        print(*prefix)
        return
    prefix = prefix or []
    for digit in range(n):
        if digit in prefix:
            continue
        prefix.append(digit)
        generate_permutation(n, m-1, prefix)
        prefix.pop()


generate_permutation(100, 600)
