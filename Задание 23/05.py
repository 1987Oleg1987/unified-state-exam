# Исполнитель Арифмометр умеет выполнять три команды:
# 1) прибавить 1;
# 2) умножить на 2;
# 3) возвести в квадрат.
#
# Сколькими способами можно получить из числа 2 число 30,
# обязательно побывав в 10 и не заходя в 14?


# Сначала посчитаем пути от 2 до 10.

A = 1000 * [0]
A[2] = 1

for i in range(2, 11):
    A[i + 1] += A[i]
    A[2 * i] += A[i]
    A[i ** 2] += A[i]

# Теперь посчитаем пути от 10 до 30, "выколов" по дороге 14.

B = 1000 * [0]
B[10] = 1

for i in range(10, 30):
    if i == 14:
        B[i] = 0
    B[i + 1] += B[i]
    B[2 * i] += B[i]
    B[i ** 2] += B[i]

print(A[10])
print(B[30])
print(A[10] * B[30])
