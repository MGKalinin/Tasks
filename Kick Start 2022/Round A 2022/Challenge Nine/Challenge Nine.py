a = [3, 4]
b = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Al = len(a)  # длина a
Bl = len(b)  # длина b
Ai = 0  # индекс a
Bi = 0  # индекс b
r=[]
# цикл по списку a, пока индекс a не больше индекс max a
while Ai<Al:
    for i in b:
        if a[Ai]<b[Bi]:
            a.insert(Ai,b[Bi])
            print(a)
        if sum(a)%9!=0:
            continue
        else:
            r.append(a)
            Ai+=1
            Bi+=1

# индекс a 0
# если b индекс 0 больше a  индекс ноль - найти сумму а
# типа Codespase ,исчё
