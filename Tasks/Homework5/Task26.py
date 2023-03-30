a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
8
def rec(a, b):
    if (b == 0):
        return 1
    elif (b == 1):
        return (a)
    else:
        return (a * rec(a, b - 1))

print(f'число {a} в степени {b} равно {rec(a, b)}')