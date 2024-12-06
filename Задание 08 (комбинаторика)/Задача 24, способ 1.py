# Определите количество 12-ричных пятизначных чисел, в записи которых
# ровно одна цифра 7 и не более трёх цифр с числовым значением, превышающим 8.

from itertools import product

counter = 0

for x in product("0123456789AB", repeat=5):
    s = "".join(x)
    if (s[0] != "0") and (s.count("7") == 1) and \
            (s.count("9") + s.count("A") + s.count("B") <= 3):
        counter += 1

print(counter)
