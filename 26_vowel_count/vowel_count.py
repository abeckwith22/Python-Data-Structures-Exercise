def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    vowelsDictionary = {}
    vowels = 'aeoiu'

    for c in phrase:
        if (c in vowels):
            if (c in vowelsDictionary):
                vowelsDictionary[c]+=1
            else:
                vowelsDictionary[c] = 1
    
    return vowelsDictionary