import math

DAILY_COINS = 50
FOOD = 2
group_size = int(input())
days = int(input())
coins_urned: int = 0

for i in range(1, days + 1):

    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5

    coins_urned += DAILY_COINS
    coins_urned -= FOOD * group_size
    has_party = False

    if i % 3 == 0:
        coins_urned -= group_size * 3
        has_party = True

    if i % 5 == 0:
        coins_urned += group_size * 20
        if has_party:
            coins_urned -= group_size * 2

    #print(f'day:{i} | group:{group_size} | coins:{coins_urned}')

print(f'{group_size} companions received {math.floor(coins_urned / group_size)} coins each.')
