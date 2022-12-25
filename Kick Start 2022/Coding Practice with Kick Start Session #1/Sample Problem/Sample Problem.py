import sys
sys.stdin = open("input_ Sample Problem.txt")

t = int(input()) 
for i in range(1, t + 1):
	n= [int(s) for s in input().split(' ')]
	C=[int(s) for s in input().split(' ')] #candy
	N=n[0] #bags
	M=n[1] #kids
		
	print(f'Case #{i}: {sum(C)%M}')
