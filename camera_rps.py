import cv2
from keras.models import load_model
import numpy as np
import random
import time


class RPS:
    
    def __init__(self):
        self.model = load_model('Teachable_Machine_keras/keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    def count_countdown(self):
        countdown = 5
        print("\nPlease prepare to show your choice")
        while countdown > 0:
            print(f'{countdown}')
            cv2.waitKey(1000)
            countdown -= 1
        print('\nShow your hand now')     

    def get_prediction(self):
        end = time.time() + 1
        while time.time() < end:
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            cv2.imshow('frame', frame)
            prediction = self.model.predict(self.data)
            choice = choices_list[prediction.argmax()]
            print(f"You chose {choice}")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return choice        

    def get_computer_choice(self):
        computer_choice = random.choice(choices_list)
        return computer_choice

    def get_winner(self, choice, computer_choice):
        if choice == computer_choice:
            print(f"Draw! The computer chose {computer_choice}. Same as you!")

        elif choice == "rock" and computer_choice == "paper":
            print(f"You lost! the computer picked {computer_choice}") 
        
        elif choice == "paper" and computer_choice == "scissors":
            print(f"You lost! the computer picked {computer_choice}")         

        elif choice == "scissors" and computer_choice == "rock":
            print(f"You lost! the computer picked {computer_choice}") 

        elif choice == "rock" and computer_choice == "scissors":
            print(f"You won! the computer picked {computer_choice}") 
        
        elif choice == "paper" and computer_choice == "rock":
            print(f"You won! the computer picked {computer_choice}")         

        elif choice == "scissors" and computer_choice == "paper":
            print(f"You won! the computer picked {computer_choice}")
        
        else:
            print("You chose nothing")
        
def play_game(choices_list):
    game = RPS()
    game.count_countdown()
    user_choice = game.get_prediction()
    computer_choice = game.get_computer_choice()
    game.get_winner(user_choice, computer_choice)

# After the loop release the cap object
    game.cap.release()
# Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    choices_list = ['rock', 'paper', 'scissors', 'nothing']
    play_game(choices_list)

