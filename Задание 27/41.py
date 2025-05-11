n = int(input())

ps = (n + 1) * [0]

for i in range(n):
    x = int(input())
    ps[i + 1] = ps[i] + x

min_left = 1_000_000
max_d = -1_000_000

for j in range(1, n + 1):
    if ps[j - 1] < min_left:
        min_left = ps[j - 1]
        i_min = j - 1
        
    d = ps[j] - min_left

    if d > max_d:
        max_d = d
        i0, j0 = i_min, j

print(max_d)
print(i0, j0 - 1)
