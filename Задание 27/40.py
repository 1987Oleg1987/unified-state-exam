n = int(input())

max_left = 116 * [-1]
max_sum = -1_000_000

x0 = int(input())

for i in range(1, n):
    s = x0 % 116
    if x0 > max_left[s]:
        max_left[s] = x0

    right_element = int(input())
    r = right_element % 116
    k = (116 - r) % 116
    
    if max_left[k] != -1 and right_element < max_left[k]:
        summ = right_element + max_left[k]
        if summ > max_sum: max_sum = summ
    x0 = right_element

print(max_sum)
