from typing import List

# the bug in parse_nested_parens is that it doesn't handle the case when there are no paren groups
# in this case, it should return 1
# to fix it, we need to add a check to see if the string is empty or not
# here is the correct implementation

def parse_nested_parens(paren_string: str) -> List[int]: