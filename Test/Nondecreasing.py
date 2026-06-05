def main():
    print("Enter a sequence of non-decreasing numbers.")

    # 1. Ask for the very first number and start the length counter at 1
    previous_number = float(input("Enter num: "))
    sequence_length = 1

    # 2. Start an infinite loop for the rest of the numbers
    while True:
        current_number =  float(input("Enter num: "))
    
        # 3. If the new number is smaller, the sequence breaks
        if current_number < previous_number:
            break

        # 4. Otherwise, increase the length and update the previous number    
        sequence_length += 1
        previous_number = current_number

    # 5. Print the exit messages
    print("Thanks for playing!")
    print(f"Sequence length: {sequence_length}")

if __name__ == "__main__":
    main()