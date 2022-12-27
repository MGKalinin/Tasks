import sys
sys.stdin = open('input_ Speed Typing.txt')

t = int(input())
for i in range(1, t + 1):
	I = input()  #оригинал
	P = input()  #продукт

	N = len(I)
	M = len(P)
	ptrI = 0
	ptrP = 0

	while ptrI < N and ptrP < M:
		if I[ptrI] == P[ptrP]:
			ptrI += 1
			ptrP += 1
		else:
			ptrP += 1
	if ptrI == N:

		print(f'Case #{i}: {M-N}')
	else:
		print(f'Case #{i}: IMPOSSIBLE')

