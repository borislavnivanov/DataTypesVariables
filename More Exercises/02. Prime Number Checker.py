import math

number = int(input())
is_prime: bool = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, math.ceil(number / 2)):
        if number % i == 0:
            is_prime = False
            break

print(is_prime)
