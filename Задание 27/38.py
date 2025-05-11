n = int(input())

min_left = 1_000_000
max_d = -1_000_000

x0 = int(input())

for i in range(1, n):
    if x0 < min_left: min_left = x0
    right_element = int(input())
    d = right_element - min_left
    if d > max_d: max_d = d
    x0 = right_element

print(max_d)
