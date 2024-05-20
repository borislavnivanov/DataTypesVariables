balls = int(input())

best_calc = int()
output = ''

for _ in range(balls):
    weight = int(input())
    time = int(input())
    quality = int(input())

    calc = (weight / time) ** quality

    if calc > best_calc:
        best_calc = calc
        output = f'{weight} : {time} = {calc:.0f} ({quality})'

print(output)
