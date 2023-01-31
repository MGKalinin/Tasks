import sys

sys.stdin = open(" Range Partition.txt")


# N set of first  positive integers
# X Alan
# Y Barbara
# SumN=(N*(N+1))/2  sum of first N positive integers
# S_Alan=SumN×(X/(X+Y))
# If SumN(mod(X+Y))≢0 then it is IMPOSSIBLE
def range_partition():
    N, X, Y = [int(s) for s in input().split(' ')]
    print(N, X, Y)
    SumN = (N * (N + 1)) / 2
    S_Alan = SumN * (X / (X + Y))
    r = []
    if SumN % (X + Y) != 0:
        return 'IMPOSSIBLE', f'{SumN % (X + Y)}'
    else:
        print(f'POSSSIBLE  SumN {SumN}, S_Alan {S_Alan}')
        for i in range(1, N + 1):
            if i <= S_Alan + 1:
                r.append(i)
                S_Alan -= i
        print(f'quantity {len(r)},list {r}')


for case in range(int(input())):
    print('Case #%d: %s' % (case + 1, range_partition()))
