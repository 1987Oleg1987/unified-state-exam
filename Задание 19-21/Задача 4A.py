def create_next_positions(A):
    B = []
    for x, y in A:
        B.append((x + 1, y))
        B.append((x, y + 1))
        B.append((x * 2, y))
        B.append((x, y * 2))
    return B


found = False
for s in range(1, 70):
    A = [(7, s)]
    B = create_next_positions(A)
    C = create_next_positions(B)
    for x, y in C:
        if x + y >= 77:
            found = True
            break
    if found:
        print(s)
        break
