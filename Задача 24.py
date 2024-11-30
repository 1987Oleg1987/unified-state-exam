# Определите количество 12-ричных пятизначных чисел, в записи которых
# ровно одна цифра 7 и не более трёх цифр с числовым значением, превышающим 8.

from itertools import product

counter = 0

for x in product("0123456789AB", repeat=5):
    s = "".join(x)

    k_7 = 0    # кол-во раз, которое в строке встречается цифра 7
    k_big = 0  # кол-во раз, которое в строке встречаются цифры 9, A и B
    for i in range(5):
        if s[i] == "7":
            k_7 += 1
        elif s[i] in "9AB":
            k_big += 1

    if (s[0] != "0") and (k_7 == 1) and (k_big <= 3):
        counter += 1

print(counter)
