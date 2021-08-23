#Solution 1

#import random

# def play():
#     user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
#     computer = random.choice(['r', 'p', 's'])

#     if user == computer:
#         return 'It\'s a tie'

#     # r > s, s > p, p > r
#     if is_win(user, computer):
#         return 'You won!'

#     return 'You lost!'

# def is_win(player, opponent):
#     # return true if player fwins
#     # r > s, s > p, p > r
#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
#         or (player == 'p' and opponent == 'r'):
#         return True

# print(play())




#Solution 2

import random

print("Lets play rock paper and scissor game")
user_wins = 0
computer_wins = 0

options = ['r', 'p' , 's']

while True:
    user_input = input("Type r for rock, p for paper and s for scissor or q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # r = 0, p = 1, s = 2
    computer_pick = options[random_number]
    print (f"Computer picked: {computer_pick}")

    if user_input == computer_pick:
        print("Its a tie!")
        continue

    if (user_input == 'r' and computer_pick == 's') or (user_input == 'p' and computer_pick == 'r') or (user_input == 's' and computer_pick == 'p'):
        print("You won!!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print(f"You win {user_wins} times")
print(f"Computer wins {computer_wins} times")

