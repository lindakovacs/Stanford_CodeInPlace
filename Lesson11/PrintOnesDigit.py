"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

# Write your helper function here!
def print_ones_digit(num):
    print("The ones digit is", num % 10)

def main():
    num = int(input("Enter a number: "))
    # Call your helper function with `num` as a parameter!
    print_ones_digit(num)
    
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()