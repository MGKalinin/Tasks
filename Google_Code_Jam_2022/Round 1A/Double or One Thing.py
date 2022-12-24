# import sys
# sys.stdin = open("input_1.txt")

def double_or_one_thing():
    S = input()
    result = []
    cnt = 1
    for i in range(len(S)):
        if i+1 != len(S):
            if S[i] == S[i+1]:
                cnt += 1
            else:
                if S[i] < S[i+1]:
                    result.append(S[i]*cnt)
                cnt = 1
        result.append(S[i])
    return "".join(result)

for case in range(int(input())):
    print(f'Case #{case+1}: {double_or_one_thing()}')
