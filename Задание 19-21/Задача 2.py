from functools import lru_cache


@lru_cache
def f(x):
    if x >= 64:
        return ('F', 0)

    a1, b1 = f(x + 1)
    a2, b2 = f(x + 2)
    a3, b3 = f(x * 3)

    if a1 == 'W' and a2 == 'W' and a3 == 'W':
        # Можно и так: if (a1, a2, a3) == ('W', 'W', 'W'):
        a = 'F'
        b = 1 + max(b1, b2, b3)
    else:
        a = 'W'
        fails = []
        if a1 == 'F': fails.append(b1)
        if a2 == 'F': fails.append(b2)
        if a3 == 'F': fails.append(b3)
        b = 1 + min(fails)

    return (a, b)


for s in range(1, 64):
    print(s, f(s))
