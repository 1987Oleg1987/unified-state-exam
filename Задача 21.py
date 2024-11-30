# Определите количество семизначных чисел, записанных в девятеричной системе счисления,
# в записи которых ровно одна цифра 8, при этом числа не начинаются с нечётных цифр
# и не оканчиваются чётными цифрами.

from itertools import product

counter = 0

for x in product("012345678", repeat=7):
    s = "".join(x)
    if (s[0] in "2468") and (s[6] in "1357") and (s.count("8") == 1):
        counter += 1

print(counter)
