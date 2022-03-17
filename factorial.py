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


print(power(2, 16))
