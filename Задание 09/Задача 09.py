# В файле электронной таблицы каждая строка содержит пять натуральных чисел.
# Определите количество строк таблицы, в которых квадрат суммы максимального и
# минимального чисел в строке больше суммы квадратов трёх оставшихся.

f = open("09.csv", "r")

k = 0

for s in f:
    A = list(map(int, s.rstrip("\n").split(";")))
    # A = [int(t) for t in s.rstrip("\n").split(";")]
    A.sort()
    if (A[0] + A[4]) ** 2 > A[1] ** 2 + A[2] ** 2 + A[3] ** 2:
        k += 1

f.close()

print(k)
