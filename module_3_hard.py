# 25|01 Дополнительное практическое задание по модулю 3

def calculate_structure_sum(data):
    summa  = 0
    if isinstance(data, dict): # Проверяем отдельный объект на тип данных "словарь"
        for key, value in data.items(): # Рекурсионный цикл для подсчета отдельных элементов словаря
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    elif isinstance(data, (list, set, tuple)): # Проверка "список-множеств-кортеж"
        for i  in data:
            summa += calculate_structure_sum(i)
    elif isinstance(data, (int, float)): # Сумма чисел
        summa += data
    elif isinstance(data, str): # Сумма длин строк
        summa += len (data)

    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)