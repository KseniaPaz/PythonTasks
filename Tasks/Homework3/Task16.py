import random

n = int(input("Введите колличество элементов в массиве:"))
list_n = [random.randint (1,10) for i in range(n)]
print(list_n)
count = 0
x = int(input("Введите число:"))
for i in range(n):
    if list_n[i]==x:
        count+=1
print(count)