key = int(input())
n = int(input())

result: str = ''

for _ in range(n):
    text = ord(input())
    result += chr(text + key)

print(result)
