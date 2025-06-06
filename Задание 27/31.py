# С клавиатуры вводится последовательность неотрицательных чисел. Сначала
# указывается количество элементов последовательности, а затем идут
# сами элементы; каждый элемент указывается в отдельной строке. Все элементы
# различны. Найти количество пар,
# которые можно составить из элементов последовательности, чтобы их
# произведение НЕ делилось на 34, а расстояние между элементами было не менее
# 4 позиций. Порядок элементов в паре значения не имеет,
# то есть (12, 39) и (39, 12) считаются одной и той же парой.

n = int(input())

count = 0  # ответ на задачу

left_k_d2_d17 = 0  # кол-во эл-тов левой области, к-рые делятся на 2 и на 17
left_k_d2_n17 = 0  # кол-во эл-тов левой области, к-рые делятся на 2, но не делятся на 17
left_k_n2_d17 = 0  # кол-во эл-тов левой области, к-рые не делятся на 2, но делятся на 17
left_k_n2_n17 = 0  # кол-во эл-тов левой области, к-рые не делятся ни на 2, ни на 17

buf = 4 * [0]

for i in range(4):
    buf[i] = int(input())

for i in range(4, n):
    right_element = int(input())

    r2, r17 = buf[0] % 2, buf[0] % 17

    if r2 == 0 and r17 == 0: left_k_d2_d17 += 1
    if r2 == 0 and r17 != 0: left_k_d2_n17 += 1
    if r2 != 0 and r17 == 0: left_k_n2_d17 += 1
    if r2 != 0 and r17 != 0: left_k_n2_n17 += 1

    s2, s17 = right_element % 2, right_element % 17

    if s2 == 0 and s17 == 0:
        count += left_k_d2_d17 + left_k_d2_n17 + left_k_n2_d17 + left_k_n2_n17

    if s2 == 0 and s17 != 0:
        count += left_k_d2_d17 + left_k_n2_d17

    if s2 != 0 and s17 == 0:
        count += left_k_d2_d17 + left_k_d2_n17

    if s2 != 0 and s17 != 0:
        count += left_k_d2_17

    for j in range(1, 4):
        buf[j - 1] = buf[j]
    buf[3] = right_element

print(count)
