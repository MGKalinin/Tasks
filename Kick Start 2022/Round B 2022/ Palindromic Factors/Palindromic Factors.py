import sys

sys.stdin = open("/workspaces/Tasks/Kick Start 2022/Round B 2022/ Palindromic Factors/input_Palindromic "
                 "Factors_ts1_.txt")


# /workspaces/Tasks/Kick Start 2022/Round B 2022/ Palindromic Factors/input_Palindromic Factors_ts1_.txt

def isPalindrome(a):
    s = str(a)
    rev = s[::-1]
    return s == rev


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    # print(n, type(n))
    r = []
    for k in range(1, n + 1):
        if n % k == 0:
            if isPalindrome(k):
                r.append(k)
    rez = len(r)

    print(f'Case #{i}: {rez}')
# time limit exceeded
# проверить до корень квадратный из числа
