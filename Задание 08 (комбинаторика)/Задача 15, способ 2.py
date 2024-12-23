# Алфавит состоит из 5 букв: {А, Г, Н, И, Я}.
# Сколько существует 5-символьных слов из букв этого алфавита,
# где никакие две гласные или согласные буквы не стоят рядом?
# (Вообще, буквы в слове могут повторяться.)

from itertools import product

alphabet = "АГНИЯ"  # все буквы алфавита (в виде строки)
A = set("АИЯ")  # множество гласных букв
B = set("ГН")   # множество согласных букв

counter = 0

for x in product(alphabet, repeat=5):
    s = "".join(x)
    M0 = {s[0], s[2], s[4]}  # множество символов строки, стоящих на чётных позициях
    M1 = {s[1], s[3]}  # множество символов строки, стоящих на нечётных позициях
    if (M0 <= A and M1 <= B) or (M0 <= B and M1 <= A):
        counter += 1

print(counter)
