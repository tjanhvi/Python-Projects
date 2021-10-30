rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(rock + "\n" + paper + "\n" + scissors)

import random

def game_win(computer, you):

    if computer == you:
        return None

    elif computer == 'r':
        
        if you == 'p':
            return False
        elif you == 's':
            return False

    elif computer == 'p':
        
        if you == 'r':
            return False
        elif you == 's':
            return True

    elif computer == 's':
        
        if you == 'r':
            return True
        elif you == 'p':
            return False

random = random.randint(1,3)

if random == 1: computer = 'r'
elif random == 2: computer = 'p'
elif random == 3: computer = 's'

you = input("Your turn:  rock(r) paper(p) or scissor(s)? \n")

a = game_win(computer, you)

print("Computer Turn:  rock(r) paper(p) or scissor(s)? \n")
print(f"Computer Choice: {computer}")
print(f"Your Choice: {you}")

if a == None:
    print("Game draw!")
elif a:
    print("You win!")
else:
    print("You lose!")

