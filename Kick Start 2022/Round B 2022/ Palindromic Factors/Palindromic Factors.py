import sys

sys.stdin = open("/workspaces/Tasks/Kick Start 2022/Round B 2022/ Palindromic Factors/input_Palindromic Factors_ts1_.txt")


def isPalindrome(a):
    s = str(a)
    rev = s[::-1]
    return s == rev


def square_root(x):
    return int(x ** 0.5)


t = int(input())
# Let a and b be two factors of A such that A=ab and a≤b.
# Then a≤A−−√. It follows that we can find all factors of A
# by checking the first A−−√ numbers only. For each factor a≤A−−√,
# the number b=Aa≥A−−√ is also a factor of A.
for i in range(1, t + 1):
    A = int(input())
    r = []
    for a in range(1, square_root(A) + 1):
        if A % a == 0:
            if isPalindrome(a):
                r.append(a)
            b = A // a
            if isPalindrome(b):
                r.append(b)

    # print(r)
    rez = len(set(r))

    print(f'Case #{i}: {rez}')
