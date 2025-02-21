from functools import lru_cache


@lru_cache
def f(x):
    if x >= 73:
        return ('F', 0)

    a1, b1 = f(x + 1)
    a2, b2 = f(x * 2)

    if a1 == 'W' and a2 == 'W':
        a = 'F'
        b = 1 + max(b1, b2)
    else:
        a = 'W'
        fails = []
        if a1 == 'F': fails.append(b1)
        if a2 == 'F': fails.append(b2)
        b = 1 + min(fails)

    return (a, b)


for s in range(1, 73):
    print(s, f(s))
