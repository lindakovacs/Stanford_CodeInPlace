import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    # TODO: Write your code here!!! :)
    # NOTE: For the autograder to work, you must generate the
    # COMPUTER's number FIRST, then the user's

    score = 0
    
    # Milestone #4: Loop for the number of rounds
    for i in range(NUM_ROUNDS):
        print(f"Round {i + 1}")
        
        # Milestone #1: Generate random numbers
        # NOTE: Computer FIRST, then User
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        
        print(f"Your number is {your_num}")
        
        # Milestone #2: Get user choice
        guess = input("Do you think your number is higher or lower than the computer's?: ")
        
        # Milestone #3 & #5: Game Logic and Scoring
        if guess == "higher":
            if your_num > computer_num:
                print(f"You were right! The computer's number was {computer_num}")
                score += 1
            else:
                print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        
        elif guess == "lower":
            if your_num < computer_num:
                print(f"You were right! The computer's number was {computer_num}")
                score += 1
            else:
                print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        
        # Milestone #5: Print current score and a blank line
        print(f"Your score is now {score}")
        print() 

    # Milestone #5: Final message
    print("Thanks for playing!")

if __name__ == "__main__":
    main()