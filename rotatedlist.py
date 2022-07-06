def count_rotations_linear(nums):
    '''
    Count rotations.

    Counts the number of ratotions made from a sorted list to get the given lis
    input using linear search technique.
    
    Args: 
    nums: list of numbers

    Return: An integer
    '''
    position = 0
    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:
            return position
        position +=1
    return 0


print(count_rotations_linear([4,5,6,1,2,3]))
