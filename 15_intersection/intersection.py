def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    len1 = len(l1)
    len2 = len(l2)

    intersections = []

    if (len1 >= len2):
        long = l1
        short = l2
    else:
        long = l2
        short = l1
    
    for i in long:
        if (i in short):
            intersections.append(i)
    
    return intersections

print(intersection([1, 2, 3], [2, 3, 4]))