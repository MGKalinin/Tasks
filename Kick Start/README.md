# Шаблоны

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
# Алгоритмы:
Поиск в глубину  
Поиск в ширину  
Бинарный поиск  
Алгоритм Дейкстры  
Жадный алгоритм   
Динамическое программирование  

# Стурктура данных:
Бинарные деревья поиска  
Приоритетные очереди  
Хэш-таблицы  

P.S.
"...но мы считаем, что лучший способ набраться опыта в конкурсах по алгоритмическому программированию — это участвовать в таких конкурсах, и участвовать часто, решая задачи из предыдущих раундов."  
[ Code Jam](https://codingcompetitions.withgoogle.com/codejam/faq)