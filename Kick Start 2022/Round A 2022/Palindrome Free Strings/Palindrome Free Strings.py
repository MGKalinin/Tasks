import sys

sys.stdin = open("input_Palindrome Free Strings.txt")  # для pycharm, тлф

# sys.stdin=open('/workspaces/Tasks/Kick Start 2022/Round A 2022/Palindrome Free Strings/input_Palindrome Free
# Strings.txt') #для Codespaces GitHub нужно скопировать  путь

probe = ['1', '0', '0', '?', '?']


def palindr(s):
    ls_ch = [ind for ind, z in enumerate(s) if z == '?']
    print(f'***{ls_ch}***')
    # заменить на 0,проверить на палиндром;заменить на 1,
    # проверитьь на палиндроме
    for i, z in enumerate(s):
        if z == '?':
            new_ch = '1'
            s[i] = new_ch
        print(s)
    return True


def d1000000():
    N = int(input())  # len str
    print(N, type(N))  # int
    S = [s for s in input().split(' ')]
    print(S)
    line = [_ for _ in S[0]]  # str
    print(line)
    for j in range(N - 4):
        new_line = line[j:j + 5]  # ['1', '0', '0', '?', '?']
        # прописать отдельную функцию которая будет проверять
        # на знаки вопроса ,заменять на 1 или 0 ;
        # проверять на палиндром и возвращать POSSIBLE/IMPOSSIBLE
        print(new_line)


for case in range(int(input())):
    print('Case #%d: %s' % (case + 1, d1000000()))

print(palindr(probe))
