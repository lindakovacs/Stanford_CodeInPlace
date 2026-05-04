"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    anton = 21  # Anton's age is given as 21 years old
    beth = 6 + anton  # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    chen = 20 + beth  # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    drew = chen + anton  # Drew is as old as Chen's age plus Anton's age, so add them together
    ethan = chen  # Ethan is the same age as Chen, so set Ethan's age equal to Chen's

   # Print out all of the ages!
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()