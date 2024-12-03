# Определите количество пятизначных чисел, записанных в восьмеричной системе
# счисления, в записи которых ровно одна цифра 6, при этом никакая нечётная цифра
# не стоит рядом с цифрой 6.

from itertools import product

counter = 0

for x in product("01234567", repeat=5):
    s = "".join(x)
    if (s[0] != "0") and (s.count("6") == 1):
        k = s.index("6")  # номер позиции, где расположена цифра "6"
        if (k == 0) and (s[1] not in "1357"):
            counter += 1
        elif (k == 4) and (s[3] not in "1357"):
            counter += 1
        elif (s[k - 1] not in "1357") and (s[k + 1] not in "1357"):
            counter += 1

print(counter)
