# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    # Loop from 1 up to and including MAX_NUMBER
    for i in range(1, MAX_NUMBER +1):
        # If the remainder of division by 2 is 0, the number is even        
        if i % 2 == 0:
            print(f"{i} is even")
        # Otherwise it's odd
        else:
            print(f"{i} is odd")

if __name__ == "__main__":
    main()