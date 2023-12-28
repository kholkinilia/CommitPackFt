from typing import List



def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    This function filters a list of strings by a prefix.
    :param strings: a list of strings
    :param prefix: a prefix
    :return: a list of strings that end with the prefix
    """
    return [x for x in strings if x.endswith(prefix)]