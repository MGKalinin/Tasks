import sys

sys.stdin = open("input_Palindrome Free Strings.txt")


def palindrome(s):
    if s == s[::-1]:
        return True
    return False


t = int(input())
for i in range(1, t + 1):
    mm = [s for s in input().split(' ')]
    s = mm[0]
    print(s)
    print(type(s))
    for index, character in enumerate(s):

# print(palindrome('madam'))
