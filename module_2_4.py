# 15|01 Цикл for. Элементы списка. Полезные функции в цикле

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_primes = True

for i in range(1, len(numbers)):
    for j in range(1, len(numbers)):
        if numbers[i] == 1:
            is_primes = False
            break
        elif numbers[i] == numbers[j]:
            break
        elif numbers[i] % numbers[j] == 0:
            is_primes = False
            break
    if is_primes:
        primes.append(numbers[i])
        is_primes = True
    elif numbers[i] > 1:
        not_primes.append(numbers[i])
        is_primes = True

print("Primes: ", primes)
print("Not Primes: ", not_primes)
