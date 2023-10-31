def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = {}

    ## creates an object and counts every number in the list
    for num in nums:
        if num in counter:
            counter[num]+=1
        else:
            counter[num] = 1
    
    ## find the largest number in the 'counter' object. dumb way of doing it, but it works
    largest = 0
    for key in counter:
        if (largest < counter[key]):
            largest = key
    
    return largest 

# print(mode([1, 2, 1]))
mode([1, 2, 1, 1, 1, 1, 1])

