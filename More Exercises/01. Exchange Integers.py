a = int(input())
b = int(input())

print(f'Before:\na = {a}\nb = {b}')

temp = a
a = b
b = temp

print(f'After:\na = {a}\nb = {b}')
