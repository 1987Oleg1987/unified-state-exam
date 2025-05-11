n = int(input())

max_left = -1_000_000
max_sum = -1_000_000

x0 = int(input())

for i in range(1, n):
    if x0 > max_left: max_left = x0
    right_element = int(input())
    if right_element < max_left:
        summ = right_element + max_left
        if summ > max_sum: max_sum = summ
    x0 = right_element

print(max_sum)
