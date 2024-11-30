# Алфавит состоит из 5 букв: {В, И, Ш, Н, Я}.
# Сколько существует 6-символьных слов из букв этого алфавита,
# где буква В встречается не более одного раза,
# а сами слова не начинаются с буквы Ш и не оканчиваются гласными буквами?
# Буквы в словах могут повторяться.

from itertools import product

counter = 0

for x in product("ВИШНЯ", repeat=6):
    s = "".join(x)
    if (s.count("В") <= 1) and (s[0] != "Ш") and (s[5] not in "ИЯ"):
        counter += 1

print(counter)
