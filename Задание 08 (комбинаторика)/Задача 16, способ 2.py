# Сколько существует десятичных пятизначных чисел, в которых все цифры различны
# и никакие две чётные или две нечётные цифры не стоят рядом?

from itertools import permutations

alphabet = "0123456789"  # все символы алфавита (в виде строки)
A = set("02468")  # множество чётных цифр
B = set("13579")  # множество нечётных цифр

counter = 0

for x in permutations(alphabet, 5):
    s = "".join(x)
    M0 = {s[0::2]}  # множество цифр, стоящих на чётных позициях
    M1 = {s[1::2]}  # множество цифр, стоящих на нечётных позициях
    if s[0] != "0" and ((M0 <= A and M1 <= B) or (M0 <= B and M1 <= A)):
        counter += 1

print(counter)
