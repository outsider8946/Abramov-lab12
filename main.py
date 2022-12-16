# №12 Внешняя многофазная сортировка
from Lab_10 import sort, merge
mas = []

fa = open("A.txt", 'w')
fb = open("B.txt", 'w')
fc = open("C.txt", 'w')
fd = open("D.txt", 'w')
fe = open("E.txt", 'w')

filesArray = [fa,fb,fc,fd,fe] # Процесс очистки данных
for i in range(len(filesArray)-1):
    filesArray[i].seek(0)
    filesArray[i].close()


s = 10 # кол-во элементов в оперативной памяти
fcur = open("CurrentFile.txt", 'r') # файл с входными данными
flag = 1
end = 0
len_file = 0
for line in fcur: # вычисление кол-ва чисел в файле
    cur_mas = line.split()
    print(cur_mas)
    len_s = len(cur_mas)
    len_file += len_s
    a = 0
    b = s
    while (len_s != b): # делим элементы по макс кол-ву в оперативной памяти.
        if b <= len_s:
            print(cur_mas)
            mas = cur_mas[a:b]
            for i in range(s):
                mas[i] = int(mas[i])
            print(mas)
            mas = sort(mas)
            for i in range(s):
                mas[i] = str(mas[i])
            print(mas)
        elif b > len_s:
            end = 1
            mas = cur_mas[a:len_s]
            for i in range(len_s-a):
                mas[i] = int(mas[i])
            print(mas)
            mas = sort(mas)
            for i in range(len_s-a):
                mas[i] = str(mas[i])
            print(mas)
        if flag == 1:
            fa = open("A.txt", 'a')
            fa.write(' '.join(mas))
            fa.write(' ')
            fa.close()
            flag = 0
            a = b
            b = b + s
            if end == 1:
                b = len_s
                end = 0
            print(b, len_s)
        else:
            fb = open("B.txt", 'a')
            fb.write(' '.join(mas))
            fb.write(' ')
            fb.close()
            flag = 1
            a = b
            b = b + s
            if end == 1:
                b = len_s
                end = 0
            print(b, len_s)
fa = open("A.txt", 'r')
fb = open("B.txt", 'r')
fc = open("C.txt", 'w')
fd = open("D.txt", 'w')
a = 0
b = s
ms_a = fa.readline().split()
l_a = len(ms_a)
ms_b = fb.readline().split()
l_b = len(ms_b)
print(l_a,l_b)
last = 'c'
while (l_a > b or l_b > b): # пока у нас есть элементы в A, которые меньше элементво B
    mas_a = ms_a[a:b]       # будем добавлять в итоговый файл элементы из A
    mas_b = ms_b[a:b]
    res = []
    temp_a = [int(mas_a[q]) for q in range(s)]
    temp_b = [int(mas_b[q]) for q in range(s)]
    flag = True
    print(temp_a, temp_b)
    i = 0
    j = 0
    k = 0
    while(flag):
        while (temp_a[i] <= temp_b[j] and k == 0):
            res.append(temp_a[i])
            i += 1
            if i == 10:
                k = 1
        else:
            res.append(temp_b[j])
            j += 1
            if j == 10:
                k = 1
        if i == 10:
            while j != 10:
                res.append(temp_b[j])
                j += 1
            flag = False
        if j == 10:
            while i != 10:
                res.append(temp_a[i])
                i += 1
            flag = False
    for q in range(len(res)):
        res[q] = str(res[q])
    stroka = ' '.join(res) + ' '
    if last == 'c':
        fc.write(stroka)
        last = 'd'
    elif last == 'd':
        fd.write(stroka)
        last = 'c'
    a += s
    b += s
    print(stroka)
fa.close()
fb.close()
fc.close()
fd.close()
fc = open("C.txt", 'r')
fd = open("D.txt", 'r')
fe = open("E.txt", 'w')
a = 0
b = 2*s
ms_c = fc.readline().split()
l_c = len(ms_c)
ms_d = fd.readline().split()
l_d = len(ms_d)
print(l_c,l_d)
last = 'a'
while (l_c >= b or l_d >= b): # тоже самое, что для файлов A и B
    mas_c = ms_c[a:b]
    mas_d = ms_d[a:b]
    res = [] # итоговый отсортированный масиив с числами
    temp_c = [int(mas_c[q]) for q in range(2*s)]
    temp_d = [int(mas_d[q]) for q in range(2*s)]
    flag = True
    print(temp_c, temp_d)
    i = 0
    j = 0
    k = 0
    while(flag):
        while (temp_c[i] <= temp_d[j] and k == 0):
            res.append(temp_c[i])
            i += 1
            if i == 20:
                k = 1
        else:
            res.append(temp_d[j])
            j += 1
            if j == 20:
                k = 1
        if i == 20:
            while j != 20:
                res.append(temp_d[j])
                j += 1
            flag = False
        if j == 20:
            while i != 20:
                res.append(temp_c[i])
                i += 1
            flag = False
    for q in range(len(res)):
        res[q] = str(res[q])
    stroka = ' '.join(res) + ' '
    if last == 'a':
        fe.write(stroka)
        last = b
    a += 2*s
    b += 2*s
    print(stroka)

