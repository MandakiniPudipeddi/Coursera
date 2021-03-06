# python3
import math


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    phi = (1 + math.sqrt(5)) / 2

    return round(pow(phi, n) / math.sqrt(5))


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
