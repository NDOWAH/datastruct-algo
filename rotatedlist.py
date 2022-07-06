def count_rotations_linear(arr):
    '''
    Count rotations.

    Counts the number of ratotions made from a sorted list to get the given lis
    input using linear search technique.
    
    Args: 
    nums: list of numbers

    Return: An integer
    '''
    position = 0
    while position < len(arr):
        if position > 0 and arr[position] < arr[position-1]:
            return position
        position +=1
    return 0


def count_rotations_binary(arr):
    '''Count rotations.
    
    Counts the number of rotations made from a sorted list to get a given list using
    binary search
    
    Args: List of numbers.
    
    Return: Integer'''
    lo, hi = 0, len(arr)-1
    mid = (lo + hi)//2
    mid_num = arr[mid]
    while lo < hi:
        if mid > 0 and arr[mid] < arr[mid-1]:
            return mid
        elif arr[mid] > arr[mid-1]:
            hi = mid -1
        else:
            lo = mid +1
    return 0


print(count_rotations_binary([3,4,5,1,2]))