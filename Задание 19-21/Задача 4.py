from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(1_000_000)


@lru_cache
def f(x, y):
    if x + y >= 77:
        return ('F', 0)

    a1, b1 = f(x + 1, y)
    a2, b2 = f(x * 2, y)
    a3, b3 = f(x, y + 1)
    a4, b4 = f(x, y * 2)

    if a1 == 'W' and a2 == 'W' and a3 == 'W' and a4 == 'W':
        # Можно и так: if (a1, a2, a3, a4) == ('W', 'W', 'W', 'W'):
        a = 'F'
        b = 1 + max(b1, b2, b3, b4)
    else:
        a = 'W'
        fails = []
        if a1 == 'F': fails.append(b1)
        if a2 == 'F': fails.append(b2)
        if a3 == 'F': fails.append(b3)
        if a4 == 'F': fails.append(b4)
        b = 1 + min(fails)

    return (a, b)


for s in range(30, 70):
    print(s, f(7, s))
