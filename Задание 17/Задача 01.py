# Рассматривается множество целых чисел, принадлежащих числовому отрезку
# [16 015; 48 989], которые делятся на 7 или 11 и не делятся на 9, 12, 13. 
# Найдите количество таких чисел и минимальное из них. 
# В ответе запишите два целых числа: сначала количество, затем минимальное
# число.

count = 0
minimum = 1_000_000

for x in range(16015, 48990):
    if (x % 7 == 0 or x % 11 == 0) and \
           x % 9 != 0 and x % 12 != 0 and x % 13 != 0:
        count += 1
        if x < minimum: minimum = x

print(count, minimum)
