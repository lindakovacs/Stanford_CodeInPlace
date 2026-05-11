import random

def main():
    print("Khansole Academy")
    
    generate_questions()
    
def generate_questions():
    correct_count = 0
    while correct_count < 3:
        number1 = random.randint(10, 99)
        number2 = random.randint(10, 99)

        print("What is", number1, "+", number2, "?")
        user_answer = int(input("Your answer: "))
        correct_answer = number1 + number2

        if user_answer == correct_answer:
            correct_count += 1
            user_answer
            print("Correct! You've gotten", correct_count, "correct in a row.\n")
        else:
            correct_count = 0
            user_answer
            print("Incorrect! The expected answer is", correct_answer,"\n")
        
        if correct_count == 3:
            print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()