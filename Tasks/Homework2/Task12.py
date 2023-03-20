a = int(input('Введите сумму чисел: '))
b = int(input('Введите произведение чисел: '))
for i in range(a):
    for j in range(b):
        if a == i + j and b == i * j:
            print('X =', i, 'Y =', j)
