# 21|01 Распаковка позиционных параметров

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(a = 2, c = "str")
print_params(b = 25)
print_params(c = [1, 2, 3])

print('-' * 20)
value_list = [False, 'ok', 4]
value_dict = {'a': 4, 'b': False, 'c': 'folk'}
print_params(*value_list)
print_params(**value_dict)

print('-' * 20)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
