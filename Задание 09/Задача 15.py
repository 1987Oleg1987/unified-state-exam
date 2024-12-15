# Файл электронной таблицы содержит результаты ежечасного измерения температуры воздуха
# на протяжении трёх месяцев. Сколько раз встречалась температура, которая равна
# минимальному значению?

f = open("15.csv", "r")

B = []

for s in f:
    A = list(map(float, s.rstrip("\n").split(";")))
    # A = [float(t) for t in s.rstrip("\n").split(";")]
    B.extend(A)

f.close()

minimum = min(B)
k = B.count(minimum)

print(k)
