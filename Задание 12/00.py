s = 68 * "B"

while ("AAA" in s) or ("BBB" in s):
    if "AAA" in s:
        s = s.replace("AAA", "B", 1)
    else:
        s = s.replace("BBB", "A", 1)

print(s)
