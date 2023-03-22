import random

n = int(input("Введите количество элементов в массиве:"))
list_n = [random.randint (1,20) for i in range(n)]
print(list_n)
x = int(input("Введите число:"))
min_numb = 0
for i in range(len(list_n)):
    if list_n[i]<x:
            if list_n[i]>min_numb:
                min_numb = list_n[i]

max_numb = 1
for i in range(len(list_n)):
    if list_n[i]>max_numb:
        max_numb = list_n[i]

for i in range(len(list_n)):
    if list_n[i]>x:
        if list_n[i]<max_numb:
            max_numb=list_n[i]

print(f'самый близкий по величине элемент массива к заданному числу:')
if min_numb>0:
    print(f'в меньшую сторону - число {min_numb}')
if x<max_numb:
    print(f'в большую сторону - число {max_numb}')