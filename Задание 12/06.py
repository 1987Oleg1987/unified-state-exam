def is_prime(x):
    if x == 0 or x == 1:
        return False
    r = int(x ** 0.5)
    for d in range(2, r + 1):
        if x % d == 0:
            return False
    return True


for n in range(0, 501):
    s = ">" + 39 * "0" + n * "1" + 39 * "2"
    while (">1" in s) or (">2" in s) or (">0" in s):
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)

    result = s.count("1") + 2 * s.count("2")
    if is_prime(result):
        print(n)
        break
