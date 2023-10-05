import random
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

user = int(input("What do you choose? 0 for Rock, 1 for Paper 1 2 for Scissors -- "))
computer = random.randint(0, 2)
print(f"Computer choose {computer}")

if user >= 3 or user < 0:
    print("Invalit Number")
elif user == 0 and computer == 2:
    print("User win!")
elif computer == 0 and user == 2:
    print("User lose")
elif computer > user:
    print("User lose")
elif computer < user:
    print("User win")
elif user == computer:
    print("It is a draw")

