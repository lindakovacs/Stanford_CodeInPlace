def main():
    """
    Calls two_sum_finder on a few sample inputs.
    You can add more test cases here to check your work!
    """
    print(two_sum([2, 7, 11, 15], 9))     # Expected: True
    print(two_sum([1, 2, 3, 4], 8))       # Expected: False
    print(two_sum([5, 5], 10))            # Expected: True
    print(two_sum([4], 8))                # Expected: False

def two_sum(nums, target):
    """
    Returns True if any two distinct elements in the list `nums`
    add up to the value `target`. Otherwise, returns False.

    Examples:
    two_sum([2, 7, 11, 15], 9) -> True
    two_sum([1, 2, 3, 4], 8) -> False
    """
    # Loop through each number in the list using its index
    for i in range(len(nums)):
        
        # Loop through the remaining numbers after index i
        for j in range(i + 1, len(nums)):
            
            # Check if the pair adds up to the target sum
            if nums[i] + nums[j] == target:
                return True
                
    # If the loops finish and no pair was found, return False
    return False

if __name__ == '__main__':
    main()
