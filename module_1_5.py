# Неизменяемые и изменяемые объекты. Кортежи
immutable_var = (1, 2.0, 'a', False)
print(immutable_var)
#immutable_var[0] = 22 # Кортеж нельзя вносить изменения по индексу,так как кортеж имеет фиксированные значения

mutable_list = [1, 3, 4, 'hi']
print(mutable_list)
mutable_list[0] = "help"
print(mutable_list)