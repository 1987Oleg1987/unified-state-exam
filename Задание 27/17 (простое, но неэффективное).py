n = int(input())

A = []

for i in range(n):
    x = int(input())
    A.append(x)

maxsum = -1

for i in range(n):
    for j in range(i + 4, n):
        summ = A[i] + A[j]
        if summ > maxsum: maxsum = summ
        # maxsum = max(maxsum, A[i] + A[j])

print(maxsum)
