def d1000000():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    result = 0
    for x in S:
        if result+1 <= x:
            result += 1
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, d1000000()))