import random


def game(user ,computer ):

  #user = user_action
    #possible_actions = ["rock", "paper", "scissors"]
  #computer = computer_action

    # user= input("Enter a choice (rock, paper, scissors): ")
    # possible_actions = ["rock", "paper", "scissors"]
    # computer = random.choice(possible_actions)
    # print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user == computer:
       print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
       if computer == "scissors":
        print("Rock smashes scissors! You win!")
       else:
        print("Paper covers rock! You lose.")
    elif user == "paper":
      if computer == "rock":
        print("Paper covers rock! You win!")
      else:
        print("Scissors cuts paper! You lose.")
    elif user == "scissors":
      if computer == "paper":
        print("Scissors cuts paper! You win!")
      else:
        print("Rock smashes scissors! You lose.")
    
while True:

  user=input("user:")
  possible_actions = ["rock", "paper", "scissors"]
  computer=random.choice(possible_actions)
  print(f"\nYou chose {user}, computer chose {computer}.\n")
  
  game(user,computer )
  play_again=input("wanna play again:")
  if play_again !="yes":
    break

