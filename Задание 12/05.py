s = ">" + 10 * "1" + 20 * "2" + 30 * "3"

while (">1" in s) or (">2" in s) or (">3" in s):
    if ">1" in s:
        s = s.replace(">1", "22>", 1)

    if ">2" in s:
        s = s.replace(">2", "2>", 1)

    if ">3" in s:
        s = s.replace(">3", "1>", 1)

result = 0

for x in s:
    if x.isdigit():
        result += int(x)

print(result)
