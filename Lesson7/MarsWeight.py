"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""
# Constant for Mars gravity relative to Earth
MARS_GRAVITY = 0.378

def main():
    # 1. Get the weight on Earth as a string
    earth_weight_str = input("Enter a weight on Earth: ")
    
    # 2. Convert the string to a float for math calculations
    earth_weight = float(earth_weight_str)

    # 3. Calculate weight on Mars
    mars_weight = earth_weight * MARS_GRAVITY

    # 4. Print results rounded to 2 decimal places
    print(f"The equivalent weight on Mars: {round(mars_weight, 2)}")

if __name__ == "__main__":
    main()