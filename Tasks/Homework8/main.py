
def show_all():
    file = open('Tasks\Homework8\sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    #print(data)
    file.close
    for i in data:
        print(i)

def add_contact():
    file = open ('Tasks\Homework8\sample.txt', 'a', encoding='UTF-8')
    data = input('Введите ФИО, телефон, комментарий (через ;):')
    data+='\n'
    file.write(data)
    file.close
    
def find_contact():
    find_string = input("Введите поисковый запрос:")
    file = open ('Tasks\Homework8\sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for index, data_str in enumerate(data):
        if find_string in data_str:
            print("found data = ", data_str)

            
def edit_contact():
    find_string = input("Введите поисковый запрос: ")
    replace_string = "Введите на что заменить: "
    file = open ('Tasks\Homework8\sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    data_new = []
    for data_str in data:
        if find_string in data_str:
            print("found data = ", data_str)
            data_new.append(replace_string)
        else:
            data_new.append(data_str)
    file.close    
    file = open ('Tasks\Homework8\sample.txt', 'w', encoding='UTF-8')   
       


                


def main_menu():
    print("Main menu")
    print("1. Показать всю книгу")
    print("2. Добавить новую запись")
    print("3. Редактировать запись")
    print("4. Поиск контакта")
    print("5. Удалить")
    print("6. Вернуться в главное меню")
    
if __name__=="__main__":
    main_menu()
    
    while True:
        choose = int(input("Введите пункт меню: "))
        if choose == 1:
            show_all()
        if choose == 2:
            add_contact()
        if choose == 3:
            edit_contact()    
        if choose == 4:
            find_contact()    
        if choose == 6:
            main_menu()