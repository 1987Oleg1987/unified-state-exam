# Алфавит состоит из 5 букв: {Л, Е, В, И, Й}.
# Сколько существует 5-символьных слов из букв этого алфавита, где все буквы различны
# и слова не начинаются с буквы Й, а также не содержат буквосочетания ЕИ?

from itertools import permutations

counter = 0

for x in permutations("ЛЕВИЙ", 5):
    s = "".join(x)
    if (s[0] != "Й") and ("ЕИ" not in s):
        counter += 1

print(counter)
