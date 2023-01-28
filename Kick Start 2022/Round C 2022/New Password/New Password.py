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

t = int(input())
for i in range(1, t + 1):
    N = [int(s) for s in input().split(' ')]
    P = [s for s in input().split(' ')]
    print(N[0],type(N[0]))
    print(P[0],type(P[0]))
    # if not (any(x.islower() for x in text)):
    for k in P[0]:
        print(k)


# print(f'Case #{i}: {N},{P} ')

