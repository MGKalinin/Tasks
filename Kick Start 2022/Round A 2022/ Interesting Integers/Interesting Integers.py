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
# S #сумма чифр

t = int(input())
for i in range(1, t + 1):
    start, finish = [int(s) for s in input().split(' ')]
    print(start, finish)
    for j in range(start, finish + 1):
        print(j)

