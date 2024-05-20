numbers = int(input())
result = 0

for _ in range(numbers):
    result += ord(input())

print('The sum equals: ' + str(result))
