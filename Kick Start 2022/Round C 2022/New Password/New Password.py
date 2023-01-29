import sys

sys.stdin = open("New Password.txt")

# t number of test cases
# N length of the old password
# P old password

# passwords must contain:
# 1.At least 7 characters.
# 2.At least one uppercase English alphabet letter.
# 3.At least one lowercase English alphabet letter.
# 4.At least one digit.
# 5.At least one special character #, @, *, &.

keys = ['#', '@', '*', '&']


def spec_ch(a):
    key = ['#', '@', '*', '&']
    for j in key:
        if j in a:
            return True
        return False


t = int(input())
for i in range(1, t + 1):
    N = [int(s) for s in input().split(' ')]
    P = [s for s in input().split(' ')]
    print(N[0], type(N[0]))
    print(P[0], type(P[0]))
    if not (any(x.islower() for x in P)):
        print('no1')
    if not (any(x.isupper() for x in P)):
        print('no2')
    if not (any(x.isdigit() for x in P)):
        print('no3')
    print(spec_ch(P))


# print(f'Case #{i}: {N},{P} ')
