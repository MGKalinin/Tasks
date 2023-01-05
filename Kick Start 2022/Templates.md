# Templates

```
import sys
sys.stdin = open("input.txt")
```


input() reads a string with a line of input, stripping the ' ' (newline) at the end.
This is all you need for most problems.
```commandline
t = int(input()) # read a line with a single integer  
for i in range(1, t + 1):
n, m = (int(s) for s in input().split(' ')) # read a list of integers, 2 in this case  
      print(f'Case #{i}: {n+m} {n*m}')  
```


```commandline
t = int(input())  
for i in range(1, t + 1):  
    printer1 = [int(s) for s in input().split(' ')]
    
    
print("Case #" + str(i) + ": " + str(c))
```



```commandline
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
```