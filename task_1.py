print('Добро пожаловать в Телефонный справочник!')
filename = "contacts.txt"
myfile = open(filename, "a+")
myfile.close


def main_menu():
    print('''\nГлавное меню:
    1. Показать все контакты
    2. Создать новый контакт
    3. Найти контакт
    4. Изменить контакт
    5. Удалить контакт
    6. Выйти
    ''')
    choice = input(f'Выберите и введите необходимый пункт меню: ')
    if choice == '1':
        myfile = open(filename, 'r+')
        filecontents = myfile.read()
        if len(filecontents) == 0:
            print('В телефонной книге отсутствуют контакты.')
        else:
            print(filecontents)
        myfile.close
        enter = input('Нажмите ENTER, чтобы продолжить. ')
        main_menu()
    elif choice == '2':
        newcontact()
        enter = input(f'Нажмите ENTER, чтобы продолжить. ')
        main_menu()
    elif choice == '3':
        searchcontact()
        enter = input(f'Нажмите ENTER, чтобы продолжить. ')
        main_menu()
    elif choice == '4':
        replacecontact()
        enter = input(f'Нажмите ENTER, чтобы продолжить. ')
        main_menu()
    elif choice == "5":
        delete()
        enter = input(f'Нажмите ENTER, чтобы продолжить. ')
        main_menu()
    elif choice == '6':
        print('До новых встреч!')
    else:
        print('Введите корректный номер пункта меню!')
        enter = input(f'Нажмите ENTER, чтобы продолжить. ')
        main_menu()


def searchcontact():
    search_name = input(f'Введите искомый контакт для поиска записи: ')
    remname = search_name[1:]
    firstchar = search_name[0]
    search_name = firstchar.upper() + remname
    myfile = open(filename, "r+")
    file_contents = myfile.readlines()

    found = False
    for line in file_contents:
        if search_name in line:
            print(f'Искомый контакт записан как:  ', end='')
            print(line)
            found = True
            break
    if found == False:
        print(f'Искомый контакт не найден: ' + search_name)


def input_firstname():
    first = input(f'Введите Фамилию: ')
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname


def input_lastname():
    last = input(f'Введите Имя: ')
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname


def newcontact():
    firstname = input_firstname()
    lastname = input_lastname()
    phone_num = input(f'Введите Номер телефона контакта: ')
    contact_details = (
        '[' + firstname + ' ' + lastname + ', ' + phone_num + ']\n')
    myfile = open(filename, "a")
    myfile.write(contact_details)
    print('Следующий контакт:\n ' + contact_details + '\nуспешно создан!')


def delete():
    delete_name = input(f'Введите Фамилию для удаления из списка контактов: ')
    with open(filename, "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if delete_name not in line:
                f.write(line)
        f.truncate()
        print('Следующий контакт:\n ' + delete_name + '\nуспешно удален!')


def replacecontact():
    repl_name = input(f'Введите, что меняем: ')
    new_name = input(f'Введите, на что меняем: ')
    with open(filename, 'r') as f:
        old_data = f.read()
        new_data = old_data.replace(repl_name, new_name)
    with open(filename, 'w') as f:
        f.write(new_data)
    print('Следующие данные:\n ' + repl_name + '\nизменены на:\n ' + new_name)


main_menu()