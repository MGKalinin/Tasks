import sys

sys.stdin = open('input_ Challenge Nine.txt')

#A.###############################
# t = int(input())
# # print(t)
# for i in range(1, t + 1):
#     N = input()
#     # print(N)
#     S = str(N)  # число в строку
#     L = len(S)  # длина строки
#     ans = []
#     for k in range(L + 1):
#         for z in range(0, 10):
#             if (k == 0 and z == 0) is False:
#                 num = S[:k] + str(z) + S[k:]
#                 if int(num) % 9 == 0:
#                     ans.append(int(num))
#                 num = S
#     print(f'Case #{i}: {min(ans)}')


# time limit exceeded


#B.###############################
# def challenge_nine(n):
#     num = str(n)
#     l = len(num)
#     answer = []
#     for i in range(l + 1):
#         for j in range(0, 10):
#             if (i == 0 and j == 0) is False:
#                 num = num[:i] + str(j) + num[i:]
#                 if int(num) % 9 == 0:
#                     answer.append(int(num))
#                 num = str(n)
#     return min(answer)
#
#
# num_cases = int(input())
# for case in range(1, num_cases + 1):
#     N = input()
#     ans = challenge_nine(N)
#     print(f'Case #{case}: {ans}')

# time limit exceeded...


#C.###############################
# 1.новое число=9-(сумма цифр числа)%9
# 2.найти цифру числа больше нового числа
# 3.вставить перед ней новое число
# 4.если все цифры числа > нового числа, то поставить в конец числа
# 4.если новое число 0, то вставить его после первой цифры числа
t = int(input())
print(t)
for i in range(1, t + 1):
    n=int(input())
    s=str(n)
    l=len(s)
    # 1.новое число=9-(сумма цифр числа)%9
    new_number=9-(sum(int(x) for x in str(n))%9)
