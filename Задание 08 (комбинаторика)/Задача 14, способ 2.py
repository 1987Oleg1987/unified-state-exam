# Алфавит состоит из 6 букв: {А, Б, В, Г, Д, Е}.
# Сколько существует 6-символьных слов из букв этого алфавита,
# которые не начинаются с гласной и не содержат двух одинаковых букв подряд?

from itertools import product

counter = 0

for x in product("АБВГДЕ", repeat=6):
    s = "".join(x)
    if (s[0] not in "АЕ") and \
            ("АА" not in s) and ("ББ" not in s) and ("ВВ" not in s) and \
            ("ГГ" not in s) and ("ДД" not in s) and ("ЕЕ" not in s):
        counter += 1

print(counter)
