# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
#     # This is all you need for most problems.
#     t = int(input()) # read a line with a single integer
#     for i in range(1, t + 1):
#       n, m = (int(s) for s in input().split(' ')) # read a list of integers, 2 in this case
#       print(f'Case #{i}: {n+m} {n*m}')

t = int(input())  # read a line with a single integer
rc = ' '
for i in range(1, t + 1):
    rc = list(map(int, input().strip().split(' ')))
    r = int(rc[0])
    c = int(rc[1])
    first_R = ('.' * 2 + ('+-' * (c - 1)) + '+\n')
    second_R = ('.' * 2 + ('|.' * (c - 1)) + '|\n')
    middle_R = (('+-' * c + '+\n') + ('|.' * c + '|\n')) * (r - 1)
    last_R = ('+-' * c + '+')
    matrix = "\n" + first_R + second_R + middle_R + last_R
    print("Case #{}: {}".format(i + 1, matrix))
