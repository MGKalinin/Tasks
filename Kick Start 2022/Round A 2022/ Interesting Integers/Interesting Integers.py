# Let us call an integer interesting if the product of
# its digits is divisible by the sum of its digits.
# You are given two integers A and B.
# Find the number of interesting integers between
# A and B (both inclusive).
import sys

sys.stdin = open("input_Interesting Integers.txt")
###########################################
# string = list(input("Введи число: "))
# output = 0
#
# for num in string:
#     output += int(num)
#
# print(output)

# Двузначное число больше 9, но меньше 100.
###########################################

# N  # число
# L  # количество цифр в числе
# P # произведение цифр
# S #сумма чифр

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [91, 92, 93, 94, 95, 96, 97, 98, 99]


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


t = int(input())
for i in range(1, t + 1):
    start, finish = [int(s) for s in input().split(' ')]

print(summ(b[1]))
print(prod(b[3]))
