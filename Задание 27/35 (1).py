n = int(input())

max_d2_d35 = -1   # максимальный элемент, делящийся на 2 и на 35
max_d2_d35_2 = -1 # второй максимальный элемент, делящийся на 2 и на 35
max_n2_d35 = -1   # максимальный элемент, не делящийся на 2, но делящийся на 35
max_n2_d35_2 = -1 # второй максимальный элемент, не делящийся на 2, но делящийся на 35
max_d2_n35 = -1   # максимальный элемент, делящийся на 2, но не делящийся на 17
max_n2_n35 = -1   # максимальный элемент, не делящийся ни на 2, ни на 35

for i in range(n):
    x = int(input())
    r2, r35 = x % 2, x % 35

    if r2 == 0 and r35 == 0:
        if x > max_d2_d35:
            max_d2_d35_2 = max_d2_d35
            max_d2_d35 = x
            # эти две строки можно совместить в одну:
            # max_d2_d35, max_d2_d35_2 = x, max_d2_d35
        elif x > max_d2_d35_2:
            max_d2_d35_2 = x

    if r2 == 0 and r35 != 0:
        if x > max_d2_n35:
            max_d2_n35 = x

    if r2 != 0 and r35 == 0:
        if x > max_d2_d35:
            max_n2_d35_2 = max_n2_d35
            max_n2_d35 = x
            # эти две строки можно совместить в одну:
            # max_n2_d35, max_n2_d35_2 = x, max_n2_d35
        elif x > max_n2_d35_2:
            max_n2_d35_2 = x

    if r2 != 0 and r35 != 0:
        if x > max_n2_n35:
            max_n2_n35 = x

maxpro = -1

if max_d2_d35 != -1 and max_d2_d35_2 != -1:
    pro = max_d2_d35 + max_d2_d35_2
    if pro > maxpro:
        maxpro = pro
        a, b = max_d2_d35, max_d2_d35_2

if max_d2_d35 != -1 and max_d2_n35 != -1:
    pro = max_d2_d35 + max_d2_n35
    if pro > maxpro:
        maxpro = pro
        a, b = max_d2_d35, max_d2_n35

if max_n2_d35 != -1 and max_n2_d35_2 != -1:
    pro = max_d2_d35 + max_n2_d35_2
    if pro > maxpro:
        maxpro = pro
        a, b = max_d2_d35, max_n2_d35_2

if max_n2_d35 != -1 and max_n2_n35 != -1:
    pro = max_n2_d35 + max_n2_n35
    if pro > maxpro:
        maxpro = pro
        a, b = max_n2_d35, max_n2_n35

if maxpro == -1:
    print("NO")
else:
    print(a, b)
    print(maxpro)
