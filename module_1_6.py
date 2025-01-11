# Словари и множества
my_dict = {'Имя': "Андрей", 'Год рождения': 2002}
print(my_dict)
print(my_dict['Имя'])
my_dict.update({'Возраст': 22, 'Пол': 'мужской'})
print(my_dict)
del my_dict['Год рождения']
print(my_dict)
print("-"*10)
my_set = {1, 2, 2, 3, "kak", "kak", False, (1, 3, "str")}
print(my_set)
my_set.add(5)
my_set.add(6)
my_set.discard(1)
print(my_set)
