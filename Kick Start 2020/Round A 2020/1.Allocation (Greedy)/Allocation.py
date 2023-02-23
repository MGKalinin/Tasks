import sys

# T test cases
# N houses, B budget
# Ai, the cost of the i-th house

sys.stdin = open(" Allocation.txt")

t = int(input())
for i in range(1, t + 1):
    N, B = [int(s) for s in input().split(' ')]
    A = [int(s) for s in input().split(' ')]
    quantity = 0
    A.sort()
    for j in range(len(A)):
        if B >= A[j]:
            quantity += 1
            B = B - A[j]

    print(f'Case #{i}: {quantity}')
