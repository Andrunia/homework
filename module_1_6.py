# Словари и множества
my_dict = {'Имя': "Андрей", 'Год рождения': 2002}
print(f"Dict: {my_dict}")
print(f"Existing item: {my_dict['Год рождения']}")
print(f"Not existing value: {my_dict.get("Никнейм")}")
my_dict.update({'Возраст': 22, 'Пол': 'мужской'})
del my_dict['Год рождения']
print(f"Deleted value: {my_dict.setdefault('Год рождения',2002)}")
print()
my_set = {1, 2, 2, 3, "kak", "kak", False, (1, 3, "str")}
print(my_set)
my_set.add(5)
my_set.add(6)
my_set.discard(1)
print(my_set)
