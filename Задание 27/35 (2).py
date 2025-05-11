n = int(input())

max_left_d2_d35 = -1
max_left_n2_d35 = -1
max_left_d2_n35 = -1
max_left_n2_n35 = -1

max_sum = -1

x0 = int(input())

for i in range(1, n):
    right_element = int(input())
    
    r2, r35 = x0 % 2, x0 % 35

    if r2 == 0 and r35 == 0:
        if x0 > max_left_d2_d35:
            max_left_d2_d35 = x0

    if r2 != 0 and r35 == 0:
        if x0 > max_left_n2_d35:
            max_left_n2_d35 = x0

    if r2 == 0 and r35 != 0:
        if x0 > max_left_d2_n35:
            max_left_d2_n35 = x0

    if r2 != 0 and r35 != 0:
        if x0 > max_left_n2_n35:
            max_left_n2_n35 = x0

    s2, s35 = right_element % 2, right_element % 35

    if s2 == 0 and s35 == 0:
        if max_left_d2_d35 != -1 and right_element + max_left_d2_d35 > max_sum:
            max_sum = right_element + max_left_d2_d35

        if max_left_d2_n35 != -1 and right_element + max_left_d2_n35 > max_sum:
            max_sum = right_element + max_left_d2_n35

    if s2 != 0 and s35 == 0:
        if max_left_n2_d35 != -1 and right_element + max_left_n2_d35 > max_sum:
            max_sum = right_element + max_left_n2_d35

        if max_left_n2_n35 != -1 and right_element + max_left_n2_n35 > max_sum:
            max_sum = right_element + max_left_n2_n35

    if s2 == 0 and s35 != 0:
        if max_left_d2_d35 != -1 and right_element + max_left_d2_d35 > max_sum:
            max_sum = right_element + max_left_d2_d35

    if s2 != 0 and s35 != 0:
        if max_left_n2_d35 != -1 and right_element + max_left_n2_d35 > max_sum:
            max_sum = right_element + max_left_n2_d35
    
    x0 = right_element

print(max_sum)
