# С клавиатуры вводится последовательность неотрицательных чисел. Сначала
# указывается количество элементов последовательности, а затем идут
# сами элементы; каждый элемент указывается в отдельной строке. Некоторые
# элементы в последовательности могут повторяться. Найти первый, второй
# и третий максимальный элементы последовательности при условии, что они
# могут совпадать.

n = int(input())

maximum = -1
maximum2 = -1
maximum3 = -1

for i in range(n):
    x = int(input())
    if x > maximum: # можно написать `>=`
        maximum3 = maximum2
        maximum2 = maximum
        maximum = x
        # эти три строки можно совместить в одну:
        # maximum, maximum2, maximum3 = x, maximum, maximum2
    elif x > maximum2: # можно написать `>=`
        maximum3 = maximum2
        maximum2 = x
        # эти две строчки можно совместить в одну:
        # maximum2, maximum3 = x, maximum2
    elif x > maximum3: # можно написать `>=`
        maximum3 = x

print(maximum, maximum2, maximum3)
