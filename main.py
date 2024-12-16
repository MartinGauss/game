import random
number = random.randint(1, 100)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

difficulty = int(input('Select difficulty where 1 is easy mode, 2 is medium mode and 3 is hard mode: '))
max_count = levels[difficulty]

user_count = int(input('Enter a number of users: '))
users = []
for i in range(user_count):
    user_name = input(f'Enter a user name: ')
    users.append(user_name)

print(users)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('All users lost')
        break
    print(f'attempt number {count}')
    for user in users:
        print(f'Stroke of {user}')
        user_number = int(input('Enter a digit: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('The digit is less')
        else:
            print('The digit is more')
else:
    print(f'The winner is {winner_name}')