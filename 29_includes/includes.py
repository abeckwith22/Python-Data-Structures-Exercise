def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    # lists/strings/sets/tuples (this sucks... there's definitely a better way of doing this but i ain't got time!)
    if isinstance(collection, (list, str, tuple, set)):
        if(start!=None and not isinstance(collection, set)):
            for i in range(len(collection)):
                if (i >= start and collection[i] == sought):
                    return True
            return False
        elif(start!=None and isinstance(collection, set)):
            return sought in collection
        else:
            return sought in collection
    elif isinstance(collection, dict):
        for key in collection:
            if(collection[key] == sought):
                return True
        return False
    else:
        return 'incorrection instance type (list, str, tuple, set, dict)'