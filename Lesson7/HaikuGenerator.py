from ai import call_gpt

"""
Write a program to create a 
Haiku, using ai.
"""

def main():
    # 1. Ask for both pieces of information inside main
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")

    print("Creating your haiku...")

    # 2. Use AI to write the haiku  
    haiku = call_gpt(f"Write a Haiku about {name} and {topic} ")
    
    # 3. Print the resulting poem    
    print(haiku)

if __name__ == "__main__":
    main()