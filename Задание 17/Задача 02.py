# В файле содержится последовательность натуральных чисел. 
# Элементы последовательности могут принимать целые значения
# от 1 до 100 000 включительно. Определите количество пар
# последовательности, в которых хотя бы одно число делится
# на минимальный элемент последовательности, кратный 21. 
# Гарантируется, что такой элемент в последовательности есть. 
# В ответе запишите количество найденных пар, затем максимальную
# из сумм элементов таких пар. В данной задаче под парой
# подразумевается два идущих подряд элемента последовательности.

f = open("File 02.txt", "r")

A = []
for s in f:
    x = int(s.rstrip('\n'))
    A.append(x)

f.close()

n = len(A)

min21 = 1_000_000

for i in range(n):
    if A[i] % 21 == 0:
        if A[i] < min21:
            min21 = A[i]

# Или так:
# for i in range(n):
#     if A[i] % 21 == 0 and A[i] < min21:
#         min21 = A[i]

# Или так:
# for i in range(n):
#     if A[i] % 21 == 0:
#         min21 = min(min21, A[i])

count = 0
maxsumm = 0

for i in range(n - 1):
    if A[i] % min21 == 0 or A[i + 1] % min21 == 0:
        count += 1
        summ = A[i] + A[i + 1]
        if summ > maxsumm:
            maxsumm = summ
        # Или так:
        # maxsumm = max(maxsumm, A[i] + A[i + 1])

print(count, maxsumm)
