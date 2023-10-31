def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    newString = ""
    index = -1
    for i in phrase:
        newString += phrase[index]
        index -= 1

    return newString
