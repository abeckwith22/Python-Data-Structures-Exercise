def reverse_vowels(string):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?'
    """
    stringVowelList= []
    vowels = ['a','e','i','o','u']
    newString = []

    for c in string: # search through string for vowels and add them to the list and modify the newString to contain a placeholder '#'
        if (c.lower() in vowels):
            stringVowelList.append(c)
            newString.append('#')
        else:
            newString.append(c)
    
    for c in range(len(newString)):
        if(newString[c] == '#'):
            val = stringVowelList.pop()
            newString[c] = val
    
    return "".join(newString)
    
