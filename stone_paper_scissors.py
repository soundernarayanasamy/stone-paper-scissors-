import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(ROCK)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.PAPER)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(scissors)
'''

items = [rock, paper, scissors]

user = int(input("What do you want to choose? Enter 0 for ROCK, 1 for PAPER, 2 for SCISSOR"))
print(items[user])

computer = random.randint(0, 2)
print("computer chooses")
print(items[computer], computer)

if user == computer:
    print("draw")
elif items[user] == "paper" and items[computer] == "rock":
    print("You Won")
elif items[user] == "scissors" and items[computer] == "paper":
    print("You Won")
elif items[user] == "rock" and items[computer] == "scissors":
    print("You Won")
else:
    print("You Loss")