import sys

# N stacks of plates
# Each stack contains K plates.
# take exactly P
# integers, describing the beauty values of each stack of plates
# from top to bottom.

sys.stdin = open(" Plates.txt")

t = int(input())
for i in range(1, t + 1):
    N, B = [int(s) for s in input().split(' ')]
    # A = [int(s) for s in input().split(' ')]

    # print(f'Case #{i}: {quantity}')
