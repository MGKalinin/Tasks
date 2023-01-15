import sys

sys.stdin = open("input_Palindrome Free Strings.txt")  # для pycharm, тлф


# sys.stdin=open('/workspaces/Tasks/Kick Start 2022/Round A 2022/Palindrome Free Strings/input_Palindrome Free
# Strings.txt') #для Codespaces GitHub нужно скопировать  путь

def verification(s):
    return len(s) <= 4 or s != s[::-1]


def palindrome(s):
    key = {i for i, z in enumerate(s) if z == '?'}
    i = 0
    rez = []
    while i < len(s):
        if i in key:
            s[i] = '0'
            rez.append(i)
        while not (verification(s[i - 4:i + 1]) and
                   verification(s[i - 5:i + 1])):
            if not rez:
                return False
            i = rez.pop()
            s[i] = '1'
        i += 1
    return True


def palindrome_free_strings():
    N = int(input().strip())
    S = list(input().strip())
    return "POSSIBLE" if palindrome(S) else "IMPOSSIBLE"


for case in range(int(input())):
    print('Case #%d: %s' % (case + 1, palindrome_free_strings()))
