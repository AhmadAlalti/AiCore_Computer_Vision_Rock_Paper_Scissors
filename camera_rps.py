import cv2
from keras.models import load_model
import numpy as np
import random


class RPS:
    
    def __init__(self):
        self.model = load_model('Teachable_Machine_keras/keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    def get_prediction(self):
        while True: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return prediction

    def get_computer_choice(self):
        computer_choice = random.choice(choices_list)
        return computer_choice

    def get_winner(self, prediction, computer_choice):
        if prediction == computer_choice:
            print(f"Draw! The computer chose {computer_choice}. Same as you!")

        elif prediction == "rock" and computer_choice == "paper":
            print(f"You lost! the computer picked {computer_choice}") 
        
        elif prediction == "paper" and computer_choice == "scissors":
            print(f"You lost! the computer picked {computer_choice}")         

        elif user_choice == "scissors" and computer_choice == "rock":
            print(f"You lost! the computer picked {computer_choice}") 

        elif user_choice == "rock" and computer_choice == "scissors":
            print(f"You won! the computer picked {computer_choice}") 
        
        elif user_choice == "paper" and computer_choice == "rock":
            print(f"You won! the computer picked {computer_choice}")         

        elif user_choice == "scissors" and computer_choice == "paper":
            print(f"You won! the computer picked {computer_choice}")
        
def play_game(choices_list):
    game = RPS(choices_list)
    user_choice = game.get_preidction()
    computer_choice = game.get_computer_choice()
    game.get_winner(user_choice, computer_choice)

if __name__ == '__main__':
    choices_list = ['rock', 'paper', 'scissors']
    play_game(choices_list)