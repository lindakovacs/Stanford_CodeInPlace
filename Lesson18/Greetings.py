"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    name = input("What's your name? ")
    print(greet(name))

# There is no need to edit code beyond this point

def greet(name):
	return "Greetings " + name + "!"
	
	
if __name__ == '__main__':
    main()