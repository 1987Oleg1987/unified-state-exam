# Алфавит состоит из 5 букв: {А, Г, Н, И, Я}.
# Сколько существует 5-символьных слов из букв этого алфавита,
# где никакие две гласные или согласные буквы не стоят рядом?
# (Вообще, буквы в слове могут повторяться.)

from itertools import product

counter = 0

for x in product("АГНИЯ", repeat=5):
    s = "".join(x)
    if (s[0] in "АИЯ") and (s[1] in "ГН") and (s[2] in "АИЯ") and \
            (s[3] in "ГН") and (s[4] in "АИЯ") or \
            (s[0] in "ГН") and (s[1] in "АИЯ") and (s[2] in "ГН") and \
            (s[3] in "АИЯ") and (s[4] in "ГН"):
        counter += 1

print(counter)
