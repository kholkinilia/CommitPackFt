from random import randint, choice
import copy
import string

letters = string.ascii_lowercase
for _ in range(100):
    str = ''.join(choice(letters) for i in range(randint(10, 20)))
    encoded_str = encode_shift(str)
    assert decode_shift(copy.deepcopy(encoded_str)) == str

# the bug in decode_shift is that it is not decoding the encoded string
# the bugged function is trying to decode the encoded string, but it is not decoding it correctly
# to fix it we need to decode the encoded string by shifting every character by 5 in the alphabet
# here is the correct implementation

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])