"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    num = 7
	# call the subtract_seven helper function here!
    num = subtract_seven(num)
    print("this should be zero: ", num)

def subtract_seven(num):
	num = num - 7
	return num

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()