import sys
from math import pi

sys.stdin = open("input_Infinity Area.txt")


def sum_areas():
    R, A, B = [int(s) for s in input().split(' ')]
    ans = R * R
    while R > 0:
        R *= A
        ans += R * R
        R //= B
        ans += R * R
    return ans * pi


for case in range(int(input())):
    print('Case #%d: %s' % (case + 1, sum_areas()))
