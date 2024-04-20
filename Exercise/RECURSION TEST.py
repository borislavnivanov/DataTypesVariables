def f(n):
    if n < 0:
        raise ValueError
    elif n == 0 or n == 1:
        return 1
    else:
        return n * f(n - 1)


print(f(5))

# F5 – n5 = 5*24 = 120
# F4 – n4 = 4*6
# F3 – n3 = 3*2
# F2 – n2 = 2*1
# F1 – n1 = 1*1
