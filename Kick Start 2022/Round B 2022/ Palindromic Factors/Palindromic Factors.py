import sys

sys.stdin = open("input_Palindromic Factors.txt")


def isPalindrome(a):
    s = str(a)
    rev = s[::-1]
    return s == rev


def square_root(x):
    return int(x ** 0.5)


# t = int(input())
# for i in range(1, t + 1):
#     n = int(input())
#     p = square_root(n)  # квадрат n
#     p_l = [x for x in range(square_root(n))]  # список от 0
#     # до квадрата n
#     print(f'это p_l {p_l}')
#     r = []
#     for k in range(1, n + 1):
#         if n % k == 0:
#             if isPalindrome(k):
#                 r.append(k)
#     print(f'это r {r}')
#     rez = len(r)
#
#     print(f'Case #{i}: {rez}')
# time limit exceeded
# проверить до корень квадратный из числа


t = int(input())
# Let a and b be two factors of A such that A=ab and a≤b.
# Then a≤A−−√. It follows that we can find all factors of A
# by checking the first A−−√ numbers only. For each factor a≤A−−√,
# the number b=Aa≥A−−√ is also a factor of A.
for i in range(1, t + 1):
    A = int(input())
    r = []

    rez = len(r)

    print(f'Case #{i}: {rez}')
