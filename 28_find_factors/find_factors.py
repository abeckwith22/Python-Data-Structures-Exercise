def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []
    for i in range(num + 1): # need to find a way of starting i at specific index
        if not i == 0:
            if (num % i == 0):
                factors.append(i)
    
    return factors

