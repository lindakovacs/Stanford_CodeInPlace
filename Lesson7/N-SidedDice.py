import random

def main():
    # 1. Ask the user for the number of sides and convert the text to an integer
    num_sides = int(input("How many sides does your dice have? "))
    
    # 2. Simulate the roll using a random number between 1 and num_sides
    roll = random.randint(1, num_sides)
    
    # 3. Print the result to the terminal
    print("Your roll is " + str(roll))

if __name__ == '__main__':
    main()