# Алфавит состоит из 6 букв: {А, Б, В, Г, Д, Е}.
# Сколько существует 6-символьных слов из букв этого алфавита,
# которые не начинаются с гласной и не содержат двух одинаковых букв подряд?

from itertools import product

counter = 0

for x in product("АБВГДЕ", repeat=6):
    s = "".join(x)
    if (s[0] not in "АЕ") and \
            (s[0] != s[1]) and (s[1] != s[2]) and (s[2] != s[3]) and \
            (s[3] != s[4]) and (s[4] != s[5]):
        counter += 1

print(counter)
