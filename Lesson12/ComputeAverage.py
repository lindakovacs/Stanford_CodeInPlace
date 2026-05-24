def main():
    number_list = load_numbers_from_file("numbers.txt")
    number_list = load_numbers_from_file("numbers.txt")
    
    # Calculate the sum of all numbers in the list
    total = sum(number_list)
    
    # Find out how many numbers are in the list
    count = len(number_list)
    
    # Compute the average
    average = total / count
    
    # Print the result exactly as requested
    print("Average:", average)

def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers

if __name__ == '__main__':
    main()
