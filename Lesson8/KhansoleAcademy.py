import random

def main():
    print("Khansole Academy")

    number1 = random.randint(10, 99)
    number2 = random.randint(10, 99)
    
    print(f"What is {number1} + {number2}?")
    user_answer = int(input("Your answer: "))

    if (number1 + number2 == user_answer):
        print("Correct!")
    else:
        print("Incorrect.")
        print("The expected answer is", number1 + number2)
    
if __name__ == '__main__':
    main()


import random

def main():
    print("Khansole Academy")
    
    generate_questions()
    
def generate_questions():
    
    correct_count = 0

    while correct_count < 3:
        number1 = random.randint(10, 99)
        number2 = random.randint(10, 99)

        print(f"What is {number1} + {number2}?")
        user_answer = int(input())
        correct_answer = number1 + number2

        if user_answer == correct_answer:
            correct_count += 1
            print("Your answer:", user_answer)
            print("Correct! You've gotten", correct_count, "correct in a row.\n")
        else:
            correct_count = 0
            print("Your answer:", user_answer)
            print("Incorrect! The expected answer is", correct_answer,"\n")
        
        if correct_count == 3:
            print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()