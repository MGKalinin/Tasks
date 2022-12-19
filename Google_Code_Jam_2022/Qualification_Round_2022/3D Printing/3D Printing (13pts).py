import sys

sys.stdin = open("input.txt")

t = int(input())
for i in range(1, t + 1):
    printer1 = [int(s) for s in input().split(' ')]
    printer2 = [int(s) for s in input().split(' ')]
    printer3 = [int(s) for s in input().split(' ')]

    c = min(printer1[0], printer2[0], printer3[0])
    m = min(printer1[1], printer2[1], printer3[1])
    y = min(printer1[2], printer2[2], printer3[2])
    k = min(printer1[3], printer2[3], printer3[3])

    r = c + m + y + k
    if r < 10 ** 6:
        print("Case #" + str(i) + ": " + "IMPOSSIBLE")
    else:
        print("Case #" + str(i) + ": " + str(c) + " " + str(m) + " " + str(y) + " " + str(k))

# Completed
