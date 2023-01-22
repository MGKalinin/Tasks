# For each factor a≤A**0.5, the number b=A/a≥A**0.5 is
# also a factor of A.
import sys

sys.stdin = open("input_Palindromic Factors.txt")


def isPalindrome(a):
    s = str(a)
    rev = s[::-1]
    return s == rev


def square_root(x):
    return int(x ** 0.5)


def division_alternative(x):
    """Функция возвращает b=x/a≥x**0.5, где a≤x**0.5"""
    sq_root = x ** 0.5  # корень квадратный
    divider = [x for x in range(1, k + 1)]
    # x/a >=k


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    p = square_root(n)  # квадрат n
    p_l = [x for x in range(square_root(n))]  # список от 0
    # до квадрата n
    print(f'это p_l {p_l}')
    r = []
    for k in range(1, n + 1):
        if n % k == 0:
            if isPalindrome(k):
                r.append(k)
    print(f'это r {r}')
    rez = len(r)

    print(f'Case #{i}: {rez}')
# time limit exceeded
# проверить до корень квадратный из числа

# 6
# 10
# 144
# 242
# print(square_root(6))
# print(square_root(10))
# print(square_root(144))
# print(square_root(242))
