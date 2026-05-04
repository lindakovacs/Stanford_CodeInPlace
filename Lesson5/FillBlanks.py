"""
Exaple of a fill in the Blank proggram
The user will enter three words (a dish, a person and an adjective).
We will then turn them into a one sentence story
"""

def main():
    dish = inout("Enter a type of food: ")
    person = input("Name a person: ")
    adjective = input("Provide an adjective: ")
    print(f"My favorite meal is {dish}, especially when it's {adjective} and coocked by {person}.")

if __name__ == '__main__':
    main()