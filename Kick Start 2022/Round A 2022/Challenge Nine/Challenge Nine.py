import sys

sys.stdin = open('input_ Challenge Nine.txt')

#A.###############################
# t = int(input())
# # print(t)
# for i in range(1, t + 1):
#     N = input()
#     # print(N)
#     S = str(N)  # число в строку
#     L = len(S)  # длина строки
#     ans = []
#     for k in range(L + 1):
#         for z in range(0, 10):
#             if (k == 0 and z == 0) is False:
#                 num = S[:k] + str(z) + S[k:]
#                 if int(num) % 9 == 0:
#                     ans.append(int(num))
#                 num = S
#     print(f'Case #{i}: {min(ans)}')


# time limit exceeded


#B.###############################
t = int(input())
for i in range(1, t + 1):
	n=int(input())
	d=(-n)%9
	s=[int(_) for _ in str(n)]
	flag=False
	for k in range(len(s)):
		if d<s[k]:
			if k==0 and d==0:
				continue
			else:
				s=s[:k]+[d]+s[k:]
				flag=True
				break
	if not flag:
		s=s+[d]
	print(f'Case #{i}: ' + ''.join(map(str, s)))
#passed
