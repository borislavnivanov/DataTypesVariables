CAPACITY = 255
tries = int(input())
fill = 0

for _ in range(tries):
    pour = int(input())
    if (fill + pour) > CAPACITY:
        print('Insufficient capacity!')
    else:
        fill += pour

print(fill)
