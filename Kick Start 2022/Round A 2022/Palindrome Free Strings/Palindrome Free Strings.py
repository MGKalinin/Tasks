import sys

#sys.stdin = open("input_Palindrome Free Strings.txt") #для pycharm, тлф
sys.stdin=open('/workspaces/Tasks/Kick Start 2022/Round A 2022/Palindrome Free Strings/input_Palindrome Free Strings.txt') #для отладчика github
 # нужно скопировать  путь


def palindrome(s):
    if s == s[::-1]:
        return True
    return False


t = int(input())
for i in range(1, t + 1):
    number = [s for s in input().split(' ')]  # кол-во символов
    print(number)
    line = [k for k in input().split(' ')]  # строка
    print(type(line[0]))  # str
    r = [x for x in line[0]]  # ['1', '0', '0', '?', '?', '?', '0', '0', '1']
    # print(r)
    for j in range(len(r) - 4):
        p = r[j:j + 5]
        # print(p)  # ['1', '0', '0', '?', '?']
        for ind, ch in enumerate(p):
            if ch == '?':
                new_z = '1'
                p[ind] = new_z  # ['1', '0', '0', '1', '?']?
                print(p)

#for i in range(len(new) - 4):
 #   f = new[i:i + 5]  # ['1', '0', '0', '?', '?']
#print(f)
#for ind, z in enumerate(f):
#    if z == '?':
#        f[ind] = d
#        print(f)
#        if pal(f):
#            print(f, 'xui')
#        else:
#            f[ind] = dd
#            if pal(f):
#                print(f, 'xui')
#            else:
#                print('dva xua')