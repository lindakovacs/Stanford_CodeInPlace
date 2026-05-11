"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    # Get user's age
    age = int(input("How old are you? "))

    # Check the user age to see where (s)he can vote
    if age >= MAYENGUA_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    elif age >= STANLAU_AGE and age < MAYENGUA_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    elif age >= PETURKSBOUIPO_AGE and age < STANLAU_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        print("You cannot vote anywhere, but maybe next year!")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()