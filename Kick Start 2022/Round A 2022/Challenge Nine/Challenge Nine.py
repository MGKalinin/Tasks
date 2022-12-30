"""Подстановка на 0 индекс исходного числа."""
a=[2,3,4]
b=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
aIndex=0
bIndex=0
rez_list=[]
while aIndex<4:
    if a[aIndex]<b[bIndex]:
        a.insert(0,b[bIndex])
        print(a)
        if sum(a)%9==0:
            print(sum(a))
            print(a)
            rez_list.append(a)
            print(rez_list)
            