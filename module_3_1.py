# 20|01 Пространство имён

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    tuple = (len(string), string.upper(), string.lower())
    return tuple


def is_contains(s, l):
    count_calls()
    return s.upper() in [n.upper() for n in l]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



