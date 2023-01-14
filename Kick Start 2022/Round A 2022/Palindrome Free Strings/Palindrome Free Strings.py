import sys

sys.stdin = open("input_Palindrome Free Strings.txt")  # для pycharm, тлф

# sys.stdin=open('/workspaces/Tasks/Kick Start 2022/Round A 2022/Palindrome Free Strings/input_Palindrome Free
# Strings.txt') #для Codespaces GitHub нужно скопировать  путь

probe = ['1', '0', '0', '?', '?']


def check_palindrome(h):
    return h == h[::-1]


def palindr(s):
    for i, z in enumerate(s):
        if z == '?':
            s[i] = '0'
            if '?' not in s:
                if check_palindrome(s):
                    s[i] = '1'
                    if check_palindrome(s):
                        return False
                return False


def d1000000():
    N = int(input())  # len str
    print(N, type(N))  # int
    S = [s for s in input().split(' ')]
    print(S)
    line = [_ for _ in S[0]]  # str
    print(line)
    for j in range(N - 4):
        new_line = line[j:j + 5]
        if palindr(new_line):
            return 'POSSIBLE'
        return 'IMPOSSIBLE'


for case in range(int(input())):
    print('Case #%d: %s' % (case + 1, d1000000()))

print(palindr(probe))
