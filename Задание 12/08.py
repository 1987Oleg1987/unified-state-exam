def sum_of_digits(s):
    result = 0
    for x in s:
        if x.isdigit():
            result += int(x)
    return result


for n in range(4, 501):
    s = ">" + 39 * "0" + n * "1" + 39 * "2"
    while (">1" in s) or (">2" in s) or (">0" in s):
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)

    if sum_of_digits(s) == 27:
        print(n)
        break
