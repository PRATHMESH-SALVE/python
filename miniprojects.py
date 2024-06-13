#Guessing the number
n=7
number_of_guess =1
print("Number of guesses is limited to only 5 times:")

while number_of_guess <=5:
    guess_number = int(input("Guess the number:"))


    if guess_number < n:
        print("you entered a leasser number , please enter a greater number")
    elif guess_number > n:
        print("you entered a greater number , please enter leasser number")
    else:
        print("you won")
        print(number_of_guess, "number of gusses took to finish")
        break

    print(5- number_of_guess,"number of gusses left")
    number_of_guess += 1

    if number_of_guess >5:
      print("game over")

# Rock paper scissor

import random

choices = ['rock', 'paper', 'scissors']

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue
        
        computer_choice = random.choice(choices)
        
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


