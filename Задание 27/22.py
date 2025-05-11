# С клавиатуры вводится последовательность неотрицательных чисел. Сначала
# указывается количество элементов последовательности, а затем идут
# сами элементы; каждый элемент указывается в отдельной строке. Некоторые
# элементы в последовательности могут повторяться. Найти два элемента
# последовательности (необязательно различные), которые отстоят друг от
# друга не менее чем на 4 позиции и при этом дают максимальное произведение,
# НЕ делящееся на 34. Если такое произведение получить не удастся,
# напишите в ответе число -1.

n = int(input()) # количество элементов последовательности

# Небольшой список (массив), в котором мы будем хранить промежуточные
# элементы, находящиеся между "левой областью" и "правым элементом"
buf = 4 * [0]

# Читаем первые 4 элемента и записываем их в ячейки буфера
for i in range(4):
    buf[i] = int(input())

max_pro = -1  # наибольшее произведение двух элементов, отстоящих на 4 и более позиции, которое не делится на 34, - ответ на вопрос задачи
a, b = -1, -1

max_left_d2_n17 = -1 # максимальный элемент "левой области", делящийся на 2, но не делящийся на 17
max_left_n2_d17 = -1 # максимальный элемент "левой области", не делящийся на 2, но делящийся на 17
max_left_n2_n17 = -1 # максимальный элемент "левой области", не делящийся ни на 2, ни на 17

# Запускаем основной цикл
for i in range(4, n):
    right_element = int(input()) # "правый элемент"

    # В левую область добавляется новый элемент: это buf[0].
    # Обновим нужные максимумы в левой области с учётом такого "пополнения".
    r2, r17 = buf[0] % 2, buf[0] % 17

    if r2 == 0 and r17 != 0:
        if buf[0] > max_left_d2_n17: max_left_d2_n17 = buf[0]

    if r2 != 0 and r17 == 0:
        if buf[0] > max_left_n2_d17: max_left_n2_d17 = buf[0]

    if r2 != 0 and r17 != 0:
        if buf[0] > max_left_n2_n17: max_left_n2_n17 = buf[0]

    # В зависимости от того, делится ли правый элемент на 2 и на 17, будем умножать его
    # на различные максимумы левой области.

    s2, s17 = right_element % 2, right_element % 17

    if s2 == 0 and s17 != 0:
        if max_left_d2_n17 != -1:
            pro = max_left_d2_n17 * right_element
            if pro > max_pro:
                max_pro = pro
                a, b = max_left_d2_n17, right_element

        if max_left_n2_n17 != -1:
            pro = max_left_n2_n17 * right_element
            if pro > max_pro:
                max_pro = pro
                a, b = max_left_n2_n17, right_element

    if s2 != 0 and s17 == 0:
        if max_left_n2_d17 != -1:
            pro = max_left_n2_d17 * right_element
            if pro > max_pro:
                max_pro = pro
                a, b = max_left_n2_d17, right_element
                
        if max_left_n2_n17 != -1:
            pro = max_left_n2_n17 * right_element
            if pro > max_pro:
                max_pro = pro
                a, b = max_left_n2_n17, right_element

    if s2 != 0 and s17 != 0:
        if max_left_d2_n17 != -1:
            pro = max_left_d2_n17 * right_element
            if pro > max_pro:
                max_pro = pro
                a, b = max_left_d2_n17, right_element

        if max_left_n2_d17 != -1:
            pro = max_left_n2_d17 * right_element
            if pro > max_pro:
                max_pro = pro
                a, b = max_left_n2_d17, right_element

        if max_left_n2_n17 != -1:
            pro = max_left_n2_n17 * right_element
            if pro > max_pro:
                max_pro = pro
                a, b = max_left_n2_n17, right_element

    # Сдвинем все элементы в буфере на одну позицию влево, чтобы
    # освободить место для нового правого элемента, который мы прочитаем
    # на следующей итерации цикла. После этого в крайнюю правую ячейку
    # буфера запишем нынешний правый элемент, поставив его на конвейер.
    for j in range(1, 4):
        buf[j - 1] = buf[j]
    buf[3] = right_element

print(max_pro)
print(a, b)
