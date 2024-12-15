# Файл электронной таблицы содержит результаты ежечасного измерения температуры воздуха
# на протяжении трёх месяцев. Определите, сколько раз за время измерений результат
# очередного измерения оказывался выше результата предыдущего на 2 и более градусов.

f = open("19.csv", "r")

B = []

for s in f:
    A = list(map(float, s.rstrip("\n").split(";")))
    # A = [float(t) for t in s.rstrip("\n").split(";")]
    B.extend(A)

f.close()

k = 0
n = len(B)

for i in range(1, n):
    if round(B[i] - B[i - 1], 1) >= 2.0:
        k += 1

# Внимание! Если в этой задаче написать просто
# if B[i] - B[i - 1] >= 2.0:
# вы получите неправильный ответ.

print(k)
