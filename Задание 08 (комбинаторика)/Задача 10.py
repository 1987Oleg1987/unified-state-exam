# Алфавит состоит из 6 букв: {А, Б, В, Г, Д, Е}.
# Сколько существует 4-символьных слов из букв этого алфавита,
# в которых буква Б встречается ровно 2 раза?
# Остальные буквы могут встречаться в слове любое количество раз
# или не встречаться вовсе.

from itertools import product

counter = 0

for x in product("АБВГДЕ", repeat=4):
    s = "".join(x)
    if s.count("Б") == 2:
        counter += 1

print(counter)
