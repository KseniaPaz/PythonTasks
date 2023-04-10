import ast

find_string = input("Введите поисковый запрос:")
file = open("Tasks\Homework8\sample1.txt", 'r', encoding='UTF-8')
data = file.readlines()
print(data)
for index, data_str in enumerate(data):
        if find_string in data_str:
              contact = data_str
              print("found data = ", contact)
my_contact = contact.split(":")
print(my_contact)
new_phone = input('Введите новый номер телефона:')
my_contact[1] = new_phone
print(my_contact)
new_contact = print(my_contact[0]+":"+" "+my_contact[1])
print(new_contact)


for index, data_str in enumerate(data):
        if find_string in data_str:
              data[index] = new_contact
              print(data[index])
print(data)

      
#res_dict = ast.literal_eval(contacts)  
#print(res_dict)
   
