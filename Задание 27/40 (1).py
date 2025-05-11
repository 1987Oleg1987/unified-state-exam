n = int(input())

max_left = 117 * [-1]
max_sum = -1_000_000

x0 = int(input())

for i in range(1, n):
    s = x0 % 117
    if x0 > max_left[s]:
        max_left[s] = x0

    right_element = int(input())
    r = right_element % 116
    k = (117 - r) % 117
    
    if max_left[k] != -1 and right_element < max_left[k]:
        summ = right_element + max_left[k]
        if summ > max_sum:
            max_sum = summ
            a, b = max_left[k], right_element
    x0 = right_element

if max_sum == -1_000_000:
    print("NO")
else:
    print(a, b)
