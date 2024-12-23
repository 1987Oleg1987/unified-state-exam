# Электронная таблица содержит результаты ежечасного измерения температуры воздуха
# на протяжении трёх месяцев. Определите, сколько раз за время наблюдений суточные
# колебания температуры (разность между максимальной и минимальной температурой
# в течение суток) превышали 17 градусов.

f = open("04.csv", "r")

k = 0

for s in f:
    A = list(map(float, s.rstrip("\n").split(";")))
    # A = [float(t) for t in s.rstrip("\n").split(";")]
    if max(A) - min(A) > 17:  # лучше так: if round(max(A) - min(A), 1) > 17.0:
        k += 1

f.close()

print(k)
