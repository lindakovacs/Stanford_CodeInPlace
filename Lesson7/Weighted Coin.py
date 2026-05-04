"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

import random

HEADS_WEIGHT = 0.7 # 70%

def main():
    # Use random.random() to generate a decimal number from 0.0 to 1.0
    # If the randomly generated number is less than 0.7 (the weight for heads), it's heads!
    if random.random() < HEADS_WEIGHT:
        print("Heads!")
    else:
        print("Tails!")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()