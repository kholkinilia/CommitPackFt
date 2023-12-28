def split_words(txt):
    """
    This function takes a string as input and splits it into a list of words.
    If the string contains a space, it splits the string at the space and returns the list of words.
    If the string contains a comma, it replaces the space with a comma and splits the string at the comma and returns the list of words.
    If the string does not contain a space or a comma, it counts the number of even-valued ASCII characters in the string and returns the count.
    """
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(' ',',').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])