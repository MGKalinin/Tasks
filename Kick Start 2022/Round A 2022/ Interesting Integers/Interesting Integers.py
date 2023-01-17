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

for j in b:
    # print(j)
    r=0
    for t in str(j):
        print(t)


t = int(input())
for i in range(1, t + 1):
    start, finish = [int(s) for s in input().split(' ')]
    # print(start, finish)
    first = []
    for j in range(start, finish + 1):
        # print(j)
        first.append(j)
    # print(first)
