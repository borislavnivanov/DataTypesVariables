lost_fights = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())

helmet_count: int = 0
cost: float = 0.00

for i in range(1, lost_fights + 1):
    helmet_flag = False
    sword_flag = False

    if i % 2 == 0:
        cost += price_helmet
        helmet_flag = True

    if i % 3 == 0:
        cost += price_sword
        sword_flag = True

    if helmet_flag and sword_flag:
        cost += price_shield
        helmet_count += 1
        if helmet_count % 2 == 0:
            cost += price_armor

print(f'Gladiator expenses: {cost:.2f} aureus')
