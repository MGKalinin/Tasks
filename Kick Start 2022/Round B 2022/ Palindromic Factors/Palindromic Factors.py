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
# For each factor a≤A**0.5, the number b=A/a≥A**0.5 is
# also a factor of A.
for i in range(1, t + 1):
    A = int(input())
    r = []
    for a in range(1, square_root(A) + 1):  # For each factor a≤A**0.5
        b = A % a
        print(f'sq_r {square_root(A)}')
        print(f'b {b}')
        if b >= square_root(A):  # the number b=A/a≥A**0.5 is
            # also a factor of A.
            r.append(b)
            print(f'first r {r}')
            if isPalindrome(b):
                r.append(b)
                print(f'second r {r}')
    print(f'это r {r}')
    rez = len(r)

    print(f'Case #{i}: {rez}')
