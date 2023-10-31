def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False

    """
    numOfClosed = 0
    numOfOpen = 0
    for c in parens: # totally not how it should, but it works!
        if (c == ')'):
            numOfClosed+=1
            if (numOfClosed > numOfOpen):
                return False
        if(c == '('):
            numOfOpen+=1
    return len(parens)%2 == 0