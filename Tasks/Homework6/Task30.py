a1=int(input('Введите первый элемент множества: '))
d=int(input('Введите разность: '))
n=int(input('Введите колличество элементов: '))
list1=[]
for i in range (1,n+1):
    list1.append(a1+(i-1)*d)
print(list1)