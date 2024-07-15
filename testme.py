j, m, add, s = 1, 1, 1, 0

for i in range(1, 17):
    if i >= m - s:
        print(j, end='')
        j -= 1

    else:
        print(j, end='')
        j += 1

    if i == m:
        print()
        add += 2
        m += add
        j = 1
        s += 1



print("--------------")

ua = {(1, (1, 2)), (0, (2,3))}
