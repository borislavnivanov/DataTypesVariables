number_people = int(input())
max_people = int(input())

full_rides = number_people // max_people
if number_people % max_people != 0:
    full_rides += 1

print(f'{full_rides}')

# if max_people > number_people:
#     print('All the people fit inside the elevator.\nOnly one course is needed.')
# else:
#     full_rides = number_people // max_people
#     remaining = number_people % max_people
#
#     print(f'{full_rides} courses * {max_people} people')
#     if remaining != 0:
#         print(f'+ 1 course * {remaining} persons')
