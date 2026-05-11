"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("Type the following affirmation: " + AFFIRMATION)

    user_affirmation = input()  # Get user's input
    while user_affirmation != AFFIRMATION:  # While the user's input isn't the affirmation
        # Tell the user that s(he) did not type the affirmation correctly
        print("That was not the affirmation.")

        # Ask the user to type the affirmation again!
        print("Type the following affirmation: " + AFFIRMATION)
        user_affirmation = input()

    print("That's right! :)")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()