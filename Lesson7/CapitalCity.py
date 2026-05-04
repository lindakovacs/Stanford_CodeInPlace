from ai import call_gpt

"""
Write a program that will tell the user 
the capital city of a country.
"""

def main():
    country = input("Country: ")
    print("Thinking...")
    capital = call_gpt(f"What is the capital of (country)? ")
    print(capital)

if __name__ == '__main__':
    main()