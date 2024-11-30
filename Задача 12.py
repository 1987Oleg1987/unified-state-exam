# Алфавит состоит из 6 букв: {А, Б, В, Г, Д, Е}.
# Сколько существует 4-символьных слов из букв этого алфавита,
# в которых буква Б встречается не менее 1 раза?

from itertools import product

counter = 0

for x in product("АБВГДЕ", repeat=4):
    s = "".join(x)
    if s.count("Б") >= 1:
        counter += 1

print(counter)
