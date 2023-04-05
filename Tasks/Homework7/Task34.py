text = input ('Винни! Запиши свой стих сюда:').lower()
phrases = text.split( )
vowels = ('аеёиоуыэюя')
sillable =[]
for i in range(len(phrases)):
    count = 0
    for j in range(len(vowels)):
        if phrases[i].count(vowels[j]) > 0:
            count += phrases[i].count(vowels[j])
    sillable.append(count)
if len(set(sillable)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')