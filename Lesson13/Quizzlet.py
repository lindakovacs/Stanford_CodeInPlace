def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    correct_count = 0
    total_words = len(translations)
    
    # Loop over each word and its translation in the dictionary
    for english_word, correct_translation in translations.items():
        # Prompt the user
        user_answer = input(f"What is the Spanish translation for {english_word}? ")
        
        # Check if the user's answer matches the correct translation
        if user_answer == correct_translation:
            print("That is correct!")
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {correct_translation}.")
            
        # Print a blank line for visual clarity
        print()
        
    # Print the final score
    print(f"You got {correct_count}/{total_words} words correct, come study again soon!")


if __name__ == '__main__':
    main()