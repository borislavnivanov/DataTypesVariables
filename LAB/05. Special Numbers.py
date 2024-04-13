n = int(input())

for i in range(1, n + 1):
    text = str(i)
    total = 0
    for element in text:
        total += int(element)

    if total == 5 or total == 7 or total == 11:
        print(f'{text} -> True')
    else:
        print(f'{text} -> False')
