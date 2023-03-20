n = int(input('Введите количество монеток: '))
count1 = 0
count2 = 0
for i in range(n):
    x = int(input('Если монета лежит решкой вверх введите любое число, если орлом, то введите 0: '))
    if x == 0:
        count1 += 1
    else:
        count2 += 1
if count1 < count2:
    print(count1)
else:
    print(count2)