import random

class RPS:

    def __init__(self, choices_list):
        self.choices_list = choices_list

    def get_user_choice(self):
        user_choice = input("Please enter your choice ")
        user_choice = user_choice.lower()
        if user_choice not in choices_list:
             print("Please enter a valid choice")

        elif user_choice in choices_list:
             print("Time for the computer to pick their choice")
        return user_choice

    def get_computer_choice(self):
        computer_choice = random.choice(choices_list)
        return computer_choice
    
    def get_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            print(f"Draw! The computer chose {computer_choice}. Same as you!")

        elif user_choice == "rock" and computer_choice == "paper":
            print(f"You lost! the computer picked {computer_choice}") 
        
        elif user_choice == "paper" and computer_choice == "scissors":
            print(f"You lost! the computer picked {computer_choice}")         

        elif user_choice == "scissors" and computer_choice == "rock":
            print(f"You lost! the computer picked {computer_choice}") 

        elif user_choice == "rock" and computer_choice == "scissors":
            print(f"You won! the computer picked {computer_choice}") 
        
        elif user_choice == "paper" and computer_choice == "rock":
            print(f"You won! the computer picked {computer_choice}")         

        elif user_choice == "scissors" and computer_choice == "paper":
            print(f"You won! the computer picked {self.computer_choice}")
            
def play_game(choices_list):
    game = RPS(choices_list)
    user_choice = game.get_user_choice()
    computer_choice = game.get_computer_choice()
    game.get_winner(user_choice, computer_choice)

if __name__ == '__main__':
    choices_list = ['rock', 'paper', 'scissors']
    play_game(choices_list)