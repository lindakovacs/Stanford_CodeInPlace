"""
Nimm is an ancient game of strategy that is named after the old German word for "take." 
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. 
Players alternate taking stones until there are zero left. 
The game of Nimm goes as follows:
1. The game starts with a pile of 20 stones between the players
2. The two players alternate turns
3. On a given turn, a player may take either 1 or 2 stone from the center pile
4. The two players continue until the center pile has run out of stones.
The last player to take a stone loses.
"""

def main():
    """
    This program simulate playing Nimm game for two players. It will determine the winner at the end.
    """
    stones = 20
    player_turn = 1
    
    while stones > 0:
        print(f"There are {stones} stones left.")
        
        # 1. Get raw input as a string first
        prompt = f"Player {player_turn} would you like to remove 1 or 2 stones? "
        user_input = input(prompt)
        
        # 2. Keep asking until we get a valid '1' or '2'
        while is_input_invalid(user_input):
            user_input = input("Enter 1 or 2: ")
            
        # 3. Now it is safe to convert to int
        num_to_remove = int(user_input)
        
        stones -= num_to_remove
        print("") # Blank line for readability
        
        # 4. Switch turns
        if player_turn == 1:
            player_turn = 2
        else:
            player_turn = 1
                
    print(f"Player {player_turn} wins!")

def is_input_invalid(user_input):
    """
    Checks if the input is NOT '1' or '2'.
    Handles letters safely because it compares strings.
    """
    if user_input == "1" or user_input == "2":
        return False
    return True

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()