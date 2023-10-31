def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'
    """
    newString = ""
    for c in phrase:
        if (c.lower() == to_swap.lower()):
            newString += c.swapcase()
        else:
            newString += c
    
    return newString
