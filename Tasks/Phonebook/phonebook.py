def print_menu():
    print("1. Показать всю книгу")
    print("2. Добавить контакт")
    print("3. Удалить контакт")
    print("4. Поиск контакта")
    print("5. Выход")
    print()

contacts = {}
menu_choice = "0"
print_menu()
while menu_choice != "5":
    menu_choice = str(input("Выберите пункт меню (1-5): "))
    if menu_choice == "1":
        file = open('Tasks\Phonebook\phonebook.txt', 'r', encoding='UTF-8')
        data = file.readlines()
        for i in data:
            print(i)

    elif menu_choice == "2":
        print("Введите ФИО и телефон")
        name = input("ФИО: ")+":"
        phone = input("Телефон: ")
        contacts[name] = phone
        
        file = open("Tasks\Phonebook\phonebook.txt", "a", encoding='UTF-8')
        mystring = ""
        for x in contacts:
            mystring = x +" " + contacts[x] + "\n"
        file.write(mystring)
        file.close()
        print()

    elif menu_choice == "3":
        print("Удалить контакт")
        name = input("ФИО: ")
        if name in contacts:
            with open("Tasks\Phonebook\phonebook.txt", "r", encoding='UTF-8') as fp:
                lines = fp.readlines()

            with open("Tasks\Phonebook\phonebook.txt", "w", encoding='UTF-8') as fp:
                for line in lines:
                    if line.strip("\n") != name + " " + contacts[name]:
                        fp.write(line)
            del contacts[name]
        else:
            print(name, "контакт не найден")
            print()

    elif menu_choice == "4":
        find_contact = input("Введите поисковый запрос:")
        file = open("Tasks\Phonebook\phonebook.txt", 'r', encoding='UTF-8')
        data = file.readlines()
        for index, data_str in enumerate(data):
            if find_contact in data_str:
                print(data_str)
        file.close      
       
    elif menu_choice != "5":
        print_menu()