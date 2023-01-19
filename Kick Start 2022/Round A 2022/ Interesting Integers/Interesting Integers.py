# Let us call an integer interesting if the product of
# its digits is divisible by the sum of its digits.
# You are given two integers A and B.
# Find the number of interesting integers between
# A and B (both inclusive).
import sys

sys.stdin = open("input_Interesting Integers.txt")


# N  # число
# L  # количество цифр в числе
# P # произведение цифр
# S # сумма чифр


def summ(n):
    """Функция суммирует цифрры числа."""
    s = 0
    for k in str(n):
        s += int(k)
    return s


def prod(n):
    """Функуия возвращает произведени цифр числа."""
    p = 1
    for j in str(n):
        p *= int(j)
    return p


def rezult():
    start, finish = [int(s) for s in input().split(' ')]
    rez = []
    for z in range(start, finish + 1):
        if prod(z) % summ(z) == 0:
            rez.append(z)
    return len(rez)


for case in range(int(input())):
    print('Case #%d: %s' % (case + 1, rezult()))

# time limit exceeded
