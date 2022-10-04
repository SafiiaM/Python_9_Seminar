# Создать информационную систему, позволяющую работать с сотрудниками некой компании \ 
# студентами вуза \ учениками школы

# Примерная функциональность для реализации:
#     получить список всех людей
#     CRUD (create-read-update-delete) для определенного человека в БД
#     импортировать / экспортировать людей в БД

# Доделать нашу мини-систему. 
# 1.txt 
# id;name;surname1;Ivan;Ivanov2;Semen;Efremov 
# 2.txt 
# id;par_id;name;surname;bd 
# 1;1;Egor;Ivanov;01.08.2022 
# 2;1;Misha;Ivanov;02.08.2022 

# ''' Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ 
# учениками школы ''' 

# database = {} 
# db = {'parents': 1, 'children': 2} 
# def reading_file_to_dict(number_file): 
#     with open(f'{number_file}.txt', 'r', encoding='utf-8') as file_1: 
#             data = [i.split('\n')[0] for i in file_1.readlines()] 
# print(database) 

# database[number_file] = [] 
# for i in data: 
#     database[number_file].append(tuple(i.split(';'))) 

# def print_children(second_name): 
#     id = [i[0] for i in database[db['parents']] if second_name in i][0] 
#     deti = [i for i in database[db['children']] if id == i[1]] 
# print(*[' '.join(i[2:4]) + '\n' for i in deti]) 

# reading_file_to_dict(1) 
# reading_file_to_dict(2) 
# print(database) 
# print_children('Ivanov') 
# # ### Создать решение для вывода детей по фамилии ###

# def show_menu() -> int:
#     print("\n" + "=" * 20)
#     print("Выберите необходимое действие")
#     print("1. Найти сотрудника")
#     print("2. Сделать выборку сотрудников по должности")
#     print("3. Сделать выборку сотрудников по зарплате")
#     print("4. Добавить сотрудника")
#     print("5. Удалить сотрудника")
#     print("6. Обновить данные сотрудника")
#     print("7. Экспортировать данные в формате json")
#     print("8. Экспортировать данные в формате csv")
#     print("9. Закончить работу")
#     return int(input("Введите номер необходимого действия: "))

# fields = ["id", "last_name", "first_name", "position", "phone_number", "salary"]


