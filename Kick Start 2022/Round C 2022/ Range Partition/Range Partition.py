import sys
sys.stdin = open(" Range Partition.txt")


def range_partition():
    N, X, Y = [int(s) for s in input().split(' ')]
    print(N, X, Y)


for case in range(int(input())):
    print('Case #%d: %s' % (case + 1, range_partition()))
