def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.capitalize() # capitalizes the first character and lowercases the rest
    newPhrase = ""
    
    needsUpper = False
    for c in phrase:
        if (needsUpper):
            newPhrase += c.upper()
            needsUpper = False
        else:
            newPhrase += c

        if (c == ' '):
            needsUpper = True
    
    return newPhrase
