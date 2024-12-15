# Сколько существует восьмеричных пятизначных чисел, не содержащих в своей записи
# цифру 1, у которых все цифры различны и никакие две чётные или две нечётные цифры
# не стоят рядом?

from itertools import permutations

alphabet = "0234567"  # все символы алфавита (в виде строки)

A = set("0246")  # множество чётных цифр
B = set("357")   # множество нечётных цифр

counter = 0

for x in permutations(alphabet, 5):
    s = "".join(x)
    M0 = {s[0], s[2], s[4]}  # множество цифр, стоящих на чётных позициях в слове
    M1 = {s[1], s[3]}  # множество цифр, стоящих на нечётных позициях в слове
    if (s[0] != "0") and ((M0 <= A and M1 <= B) or (M0 <= B and M1 <= A)):
        counter += 1

print(counter)
