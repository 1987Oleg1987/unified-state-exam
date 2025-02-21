from functools import lru_cache


@lru_cache
def f(x, y):
    if x + y >= 36:
        return ('F', 0)

    a1, b1 = f(x + y, y)
    a2, b2 = f(x, x + y)

    if a1 == 'W' and a2 == 'W':
        # Можно и так: if (a1, a2) == ('W', 'W'):
        a = 'F'
        b = 1 + max(b1, b2)
    else:
        a = 'W'
        fails = []
        if a1 == 'F': fails.append(b1)
        if a2 == 'F': fails.append(b2)
        b = 1 + min(fails)

    return (a, b)


for s in range(1, 25):
    print(s, f(9, s))
