def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    typeOf = ''
    keys = d

    for a in d:
        if(isinstance(a, int)):
            typeOf = 'int'
        if(isinstance(a, str)):
            typeOf = 'str'
        break
    
    if (typeOf == 'int'):
        maxKey = -1
        minKey = 100000000
        for key in keys:
            if key > maxKey:
                maxKey = key
            elif key < minKey:
                minKey = key
        
        return (minKey, maxKey)
    
    if (typeOf == 'str'):
        maxKey = ''
        minKey = ' '*1000000
        for key in keys:
            if len(key) > len(maxKey):
                maxKey = key
            if len(key) < len(minKey):
                minKey = key
        
        return (minKey, maxKey)

        
