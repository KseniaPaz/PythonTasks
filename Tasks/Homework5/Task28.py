a = int(input('Введите первое неотрицательное число: '))
b = int(input('Введите второе неотрицательное число: '))
def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)
print(f'Сумма равна - {sum(a, b)}')