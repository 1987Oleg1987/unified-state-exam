# Алфавит состоит из 6 букв: {А, Б, В, Г, Д, Е}.
# Сколько существует 4-символьных слов, в которых буква Б либо не встречается вовсе, либо
# стоит только на последней позиции? Предполагается, что любая буква может встречаться
# в слове сколько угодно раз или не встречаться вовсе.

from itertools import product

counter = 0

for x in product("АБВГДЕ", repeat=4):
    s = "".join(x)
    if ("Б" not in s) or (s.count("Б") == 1 and s[3] == "Б"):
        counter += 1

print(counter)
