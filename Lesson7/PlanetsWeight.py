"""
Prompts the user for a weight on Earth
and prints the equivalent weight on other Planets.
"""

# Constants for planetary gravity relative to Earth
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    try:
        earth_weight = float(input("Enter a weight on Earth: "))
        planet = input("Enter a planet: ").lower().strip()

        # Initialize the multiplier variable
        multiplier = 0

        # 1. Determine the multiplier based on the planet
        if planet == "mercury":
            multiplier = MERCURY_GRAVITY
        elif planet == "venus":
            multiplier = VENUS_GRAVITY
        elif planet == "mars":
            multiplier = MARS_GRAVITY
        elif planet == "jupiter":
            multiplier = JUPITER_GRAVITY
        elif planet == "saturn":
            multiplier = SATURN_GRAVITY
        elif planet == "uranus":
            multiplier = URANUS_GRAVITY
        elif planet == "neptune":
            multiplier = NEPTUNE_GRAVITY
        else:
            print(f"Error: '{planet}' is not recognized.")
            return # Exit the function early if the planet is wrong

        # 2. Perform the calculation once
        destination_weight = earth_weight * multiplier

        # 3. Print the result once
        print(f"The equivalent weight on {planet.capitalize()}: {round(destination_weight, 2)}")

    except ValueError:
        print("Error: Enter a valid number for the weight.")

# # Constants for planetary gravity relative to Earth using dictionaries
# GRAVITY_MAP = {
#     "mercury": 0.376,
#     "venus": 0.889,
#     "mars": 0.378,
#     "jupiter": 2.36,
#     "saturn": 1.081,
#     "uranus": 0.815,
#     "neptune": 1.14
# }

# def main():
#     try:
#         # 1. Get and convert weight
#         earth_weight = float(input("Enter a weight on Earth: "))
        
#         # 2. Get planet name
#         planet = input("Enter a planet: ").lower().strip()

#         # 3. Check if the planet exists in our dictionary
#         if planet in GRAVITY_MAP:
#             multiplier = GRAVITY_MAP[planet]
#             destination_weight = earth_weight * multiplier
            
#             # One print statement to rule them all
#             print(f"The equivalent weight on {planet.capitalize()}: {round(destination_weight, 2)}")
#         else:
#             print(f"Error: '{planet}' is not in our database.")
            
#     except ValueError:
#         print("Error: Enter a valid numerical weight.")

if __name__ == "__main__":
    main()