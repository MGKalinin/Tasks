n=234
str_n=str(n)
len_n=len(str_n)
for i in range(str_n+1): #проход по длине исходного числа
    for k in range(0,10): #проход по диапазону чисел от 10 до 10
        #первая цифра из добавленного числе не должна быть равна 0
        #вставить цифры в строку по индексу,привести к int и проверить % ==0