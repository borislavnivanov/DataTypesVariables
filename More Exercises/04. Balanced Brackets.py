n = int(input())

open_p = 0

for _ in range(n):
    text = input()
    if text == '(':
        open_p += 1
    elif text == ')':
        open_p -= 1

    if open_p > 1 or open_p < 0:
        break

if open_p != 0:
    print('UNBALANCED')
else:
    print('BALANCED')
