import random

class RPS:

    def __init__(self, choices_list):
        self.computer_choice = random.choice(choices_list)
        self.user_choice = str
        self.winner = str

    def get_user_choice(self, user_choice):
        while True:
            user_choice = input("Please enter your choice ")
            user_choice = user_choice.lower()
            if user_choice not in choices_list:
                print("Please enter a valid choice")

            elif user_choice in choices_list:
                print("Time for the computer to pick their choice")
                return user_choice

    def get_computer_choice(self, computer_choice):
        return computer_choice
    
    def get_winner(self, computer_choice, user_choice):
        if self.user_choice == self.computer_choice:
            print(f"Draw! The computer chose {self.computer_choice}. Same as you!")

        elif self.user_choice == "rock" and self.computer_choice == "paper":
            print(f"You lost! the computer picked {self.computer_choice}") 
        
        elif self.user_choice == "paper" and self.computer_choice == "scissors":
            print(f"You lost! the computer picked {self.computer_choice}")         

        elif self.user_choice == "scissors" and self.computer_choice == "rock":
            print(f"You lost! the computer picked {self.computer_choice}") 

        elif self.user_choice == "rock" and self.computer_choice == "scissors":
            print(f"You won! the computer picked {self.computer_choice}") 
        
        elif self.user_choice == "paper" and self.computer_choice == "rock":
            print(f"You won! the computer picked {self.computer_choice}")         

        elif self.user_choice == "scissors" and self.computer_choice == "paper":
            print(f"You won! the computer picked {self.computer_choice}")
            
def play_game(choices_list):
    game = RPS(choices_list)
    game.get_user_choice(game.user_choice)
    game.get_computer_choice(game.computer_choice)
    game.get_winner(game.computer_choice, game.user_choice)

if __name__ == '__main__':
    choices_list = ['rock', 'paper', 'scissors']
    play_game(choices_list)