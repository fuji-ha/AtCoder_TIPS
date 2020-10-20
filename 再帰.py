def sum_r(s):
    if s == 0:
        return s
    return sum_r(s-1)+s

print([sum_r(i) for i in range(1,7)])
