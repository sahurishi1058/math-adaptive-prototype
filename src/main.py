# importing necessary modules and functions
import time
from tracker import Tracker
from puzzle_generator import generate_puzzle
from adaptive_engine import game_engine
def main():
    print("Welcome to the Adaptive Puzzle Game!")
    print("Type 'exit' anytime to quit.\n")
    name=input("Enter your name: ")
    print(f"Hello, {name}! Let's start the game.\n")
    tracker=Tracker() # creating an object of Tracker class to keep track of user performance
    curr_level=int(input("Enter your starting level [1 Easy 2 Medium 3 Hard ] : ")) # starting level
    while True: # this loop generates the puzzle and also determines the correct answer based on the user level and further processes the user input. 
        num1,num2,operator=generate_puzzle(curr_level) 
        if operator=='+':
            correct_answer=num1+num2
        elif operator=='-':
            correct_answer=num1-num2
        elif operator=='*':
            correct_answer=num1*num2
        elif operator=='/':
            correct_answer=num1//num2 if num2!=0 else 0
        else:
            correct_answer=0
        print(f"Solve: {num1} {operator} {num2}") # displaying the puzzle to the user
        start_time=time.time() # starting the timer
        usr_input=input("Your answer: ")# taking user input
        end_time=time.time()# stopping the timer
        if usr_input.lower()=='exit': # condition to exit the game and display the performance summary
            print(f"Exiting the game {name}. Here's your performance summary:")
            tracker.get_history() # calling the function to display the performance summary
            break
        try: # checking if the user input is a valid number
            ans=int(usr_input)
        except ValueError:
            print("Enter a valid number")
            continue
        time_taken=end_time-start_time # calculating the time taken by the user to answer
        is_correct=(ans==correct_answer) # checking if the user answer is correct
        if is_correct:# displaying appropriate message based on user answer
            print(f"Correct! ({time_taken:.2f} seconds)")
        else:
            print(f"Incorrect! The correct answer was {correct_answer}.")
        tracker.log(curr_level,ans,correct_answer,time_taken) # logging the attempt in the tracker
        n_lvl,act=game_engine(curr_level,is_correct,time_taken) # calling the game_engine function to decide the next level
        if act=="Increase": # if the user answers correctly and the level increases
            print("Great job! Moving to a higher difficulty level.")
        elif act=="Decrease": # if the user answers incorrectly and the level decreases
            print("Let's try an easier level.")
        curr_level=n_lvl # updating the current level
if __name__=="__main__":
    main()