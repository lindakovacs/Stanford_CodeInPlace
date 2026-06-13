MAX_VALUE = 17

def main():
    # modify this starter code to call fizzbuzz
    # on every number from 1 to MAX_VALUE
    # Loop from 1 up to and including MAX_VALUE
    for i in range(1, MAX_VALUE + 1):
        to_say = fizzbuzz(i)
        print(to_say)

def fizzbuzz(n):
    """
    Takes in a positive integer (n) and returns
    what the player should say at that value.
    Here are a few examples:
    fizzbuzz(3) returns "Fizz"
    fizzbuzz(15) returns "Fizzbuzz"
    fizzbuzz(2) returns 2
    """
    # Check if divisible by both 3 and 5 first!
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

if __name__ == '__main__':
    main()