def string_to_md5(text):
    import hashlib
    return hashlib.md5(text).hexdigest() if text else None

# The bug in the original function was that it was not handling empty strings correctly.
# To fix this, we need to add a check for an empty string.