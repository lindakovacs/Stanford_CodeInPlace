import random

NUM_PAIRS = 3

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    # Milestone 1: Create the truth list
    truth_list = []
    for i in range(NUM_PAIRS):
        truth_list.append(i)
        truth_list.append(i)
        
    # Milestone 2: Shuffle the list
    random.shuffle(truth_list)
    
    # Milestone 3: Create the displayed list
    displayed_list = ['*'] * (NUM_PAIRS * 2)
    
    # Milestone 6: Play multiple turns until the game is won
    pairs_found = 0
    while pairs_found < NUM_PAIRS:
        # 1. Print out the display array
        print(displayed_list)
        
        # 2. Get two valid indices from the user
        idx1 = get_valid_index(displayed_list)
        idx2 = get_valid_index(displayed_list, idx1)
        
        # 3 & 4. Check for a match
        if truth_list[idx1] == truth_list[idx2]:
            print("Match!")
            displayed_list[idx1] = truth_list[idx1]
            displayed_list[idx2] = truth_list[idx2]
            pairs_found += 1
            clear_terminal()
        else:
            print(f"Value at index {idx1} is {truth_list[idx1]}")
            print(f"Value at index {idx2} is {truth_list[idx2]}")
            print("No match. Try again.")
            input("Press Enter to continue...")
            clear_terminal()
            
    # When the game is won
    print(displayed_list)
    print("Congratulations! You won!")

def get_valid_index(displayed_list, first_index=-1):
    """
    Milestone 4: Helper function that continually prompts the user until 
    they enter a valid index following all the rules.
    """
    while True:
        val = input("Enter an index: ")
        
        # Check if the input is a valid number
        try:
            idx = int(val)
        except ValueError:
            print("Not a number. Try again.")
            continue
        
        # Check if out-of-bounds
        if idx < 0 or idx >= len(displayed_list):
            print("Invalid index. Try again.")
            continue
            
        # Check if they entered the same index twice
        if idx == first_index:
            print("You entered the same index twice. Try again.")
            continue
            
        # Check if the index is already matched
        if displayed_list[idx] != '*':
            print("This number has already been matched. Try again.")
            continue
            
        # If all checks pass, return the valid index
        return idx

def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()