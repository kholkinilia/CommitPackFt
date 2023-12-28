def remove_vowels(text):
    """
    This function removes all vowels from the input text.
    """
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u", "w", "y"]])