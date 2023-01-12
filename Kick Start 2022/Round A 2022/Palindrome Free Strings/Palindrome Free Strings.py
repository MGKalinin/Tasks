import sys

sys.stdin = open("input_Palindrome Free Strings.txt")  # для pycharm, тлф


# sys.stdin=open('/workspaces/Tasks/Kick Start 2022/Round A 2022/Palindrome Free Strings/input_Palindrome Free
# Strings.txt') #для Codespaces GitHub нужно скопировать  путь


def palindr(s):
    return s == s[::-1]


d0 = '0'
d1 = '1'

t = int(input())
for i in range(1, t + 1):
    number = [s for s in input().split(' ')]  # кол-во символов
    # print(number)
    line = [k for k in input().split(' ')]  # строка
    # print(type(line[0]))
    new_line = [x for x in line[0]]
    print(f'это new_line {new_line}')  # ['1', '0', '0', '?', '?', '?', '0', '0', '1']
    for j in range(len(new_line) - 4):
        f = new_line[j:j + 5]  # f= ['1', '0', '0', '?', '?']
        print(f'это f {f}')
        for ind, z in enumerate(f):
            if z == "?":  # заменить все знаки ? на 1 или 0,затем проверить на палиндром
                f[ind] = d1
                if palindr(f):
                    f[ind] = d0
            else:
                print('poss')


ff = ['1', '0', '0', '?', '?']
fff = ['1' if x == '?' else x for x in ff]  # y = [0 if x==1 else x for x in y]

print(f'это fff {fff}')
