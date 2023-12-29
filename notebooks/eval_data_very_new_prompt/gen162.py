from typing import List

# the bug in string_to_md5 is that it uses the md5 hash function to convert the string to a hash.
# the md5 hash function is not suitable for converting strings to hashes.
# instead, we should use the sha256 hash function.
# here is the correct implementation

def string_to_md5(text):
    import hashlib
    return hashlib.sha256(text.encode()).hexdigest() if text else None