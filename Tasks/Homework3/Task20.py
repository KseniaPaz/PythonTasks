list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",2:"DGДКЛМПУ",3:"BCMPБГЁЬЯ",4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",8:"JXШЭЮ",10:"QZФЩЪ"}

word = input("Введите слово: ").upper()
sum = 0
for i in word:
    for j, k in list_letters.items():
        if i in k:
            sum += j
print(f"Стоимость введенного слова: {sum}")