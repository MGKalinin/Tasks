import sys

sys.stdin = open("input_Palindrome Free Strings.txt")


def palindrome(s):
    if s == s[::-1]:
        return True
    return False


t = int(input())
for i in range(1, t + 1):
    number = [s for s in input().split(' ')]  # кол-во символов
    line = [k for k in input().split(' ')]  # строка
    # print(number, type(number))  # list
    # print(line, type(line))
    # print(type(line[0]))  # str
    for k in line:
        for z in k:  # одна из строк
            if z == '?':
                print(z)
