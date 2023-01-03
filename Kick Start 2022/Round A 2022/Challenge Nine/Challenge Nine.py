import sys

sys.stdin = open('input_ Challenge Nine.txt')

t = int(input())
# print(t)
for i in range(1, t + 1):
    N = input()
    # print(N)
    S = str(N)  # число в строку
    L = len(S)  # длина строки
    ans = []
    for k in range(L + 1):
        for z in range(0, 10):
            if (k == 0 and z == 0) is False:
                num = S[:k] + str(z) + S[k:]
                if int(num) % 9 == 0:
                    ans.append(int(num))
                num = S
    print(f'Case #{i}: {min(ans)}')
# time limit exceeded
