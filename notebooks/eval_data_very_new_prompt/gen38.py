from typing import List

# the bug in decode_cyclic is that it is not cycling the groups of characters
# the groups are cycled in the wrong order, so the decoded string is not the same as the original
# to fix it we need to reverse the groups after cycling
# here is the correct implementation

def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)