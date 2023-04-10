def show_all():
    file = open('Tasks\Homework8\sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    #print(data)
    file.close
    
    for i in data:
        print(i)