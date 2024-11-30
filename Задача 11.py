# Алфавит состоит из 6 букв: {А, Б, В, Г, Д, Е}.
# Сколько существует 5-символьных слов из букв этого алфавита,
# в которых буква Б встречается ровно 3 раза?

from itertools import product

counter = 0

for x in product("АБВГДЕ", repeat=5):
    s = "".join(x)
    if s.count("Б") == 3:
        counter += 1

print(counter)
