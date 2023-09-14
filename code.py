def add_data():
    with open('logins.txt','a') as file:
        global add
        a = input('Введите Логин Который Вы Хотите Добавить:').lower()
        b = input('Введите Пароль Который Вы Хотите Добавить: ').lower()
        add = file.write(a + ' ' +b + '\n')
        with open ('logins.txt','r') as file:
            add = file.readline()
            add.replace('\n' ,'')
            print(add)
        with open('logins.txt','r') as file:
            add = add.split()
            print(add)
add_data()