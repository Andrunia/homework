# 15|01 Стиль кода. Цикл While. 1.2

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0

while my_list[i] > 0 or i < len(my_list):
    if my_list[i] < 0:
        break
    elif my_list[i] != 0:
        print(my_list[i])
        i += 1
    else:
        i += 1

