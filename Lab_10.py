#  №10 Сортировка слиянием
# import random
#
# n = int(input())  # Сортировка заключается в рекурсивном делении массива на подмассивы до тех опр пока длина не станет
# mas = []  # равна 1 и сравнивании 2 элементов, далее по возрастанию длины массива сравниваем все элементы
#      # O(nlogn)
#
# for i in range(n):
#     mas.append(random.randint(1, 100))
# print(mas)


def merge(left, right):
    res = []           # промежуточный массив, в который записываем слияние
    i = 0
    j = 0
    while i < len(left) and j < len(right):  # Проверка на наличие элементов в подмассивах
        if left[i] < right[j]:  # элемент из левого подмассива меньше чем из правого
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):      # Дозаписываем оставшиеся элементы в один из подмассивов если другой уже прошли
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res  # Возвращаем массив слияния


def sort(mas):
    if len(mas) < 2:
        return mas[:]
    else:
        middle = int(len(mas) / 2)
        left = sort(mas[:middle])  # Левый подмассив
        right = sort(mas[middle:])  # Правый подмассив
        return merge(left, right)  # Сортировка слиянием левого и правого подмассивов


#print(sort(mas))
