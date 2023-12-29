COMMIT_PACK_FT_DATASET = 'bigcode/commitpackft'  # a dataset path
COMMIT_PACK_FT_LANG = ['python', 'javascript', 'java', 'go', 'c++', 'rust']

HUMAN_EVAL_PACK_DATASET = 'bigcode/humanevalpack'
HUMAN_EVAL_PACK_LANG = ['python', 'js', 'java', 'go', 'cpp', 'rust']  # a list of languages we look at

PYTHON, JAVASCRIPT, JAVA, GO, CPP, RUST = range(6)  # language indexes. Useful for doing this: dataset[PYTHON]

REFACT_MODEL = "smallcloudai/Refact-1_6B-fim"

REFACT_PROMPT_TEMPLATE = "<empty_output>SYSTEM {system}\n" \
                         "<empty_output>USER {user}\n" \
                         "<empty_output>ASSISTANT"

REFACT_SYSTEM_PROMPT = """
You are a programming assistant that generates bug fixes for Python functions. A user will provide you with a function and will provide some testcases in the following format: '<function definition>[whitespace]<testcase definition>[whitespace]<instruction to fix bugs>'. You need to generate code of the correct implementation of the function. 
""".strip()

REFACT_SYSTEM_NEW_PROMPT = """
You are a programming assistant that generates bug fixes for Python functions. A user will provide you with a bugged function and will provide some testcases in the following format: '<bugged_function>[whitespace]<check_function>[whitespace]<fix_instruction>', where "bugged_function" is the function you need to corred, "check_function" is the function with testcases that the correct solution must pass, "fix_instruction" is the instruction to fix a bug.  
Your response should be in the following format: '<imports>[whitespace]<description_comment>[whitespace]<correct implementation>', where "imports" are required imports, "description_comment" is a python comment that describes a bug and a way to fix it with natural language, "correct_implementation" is the correct implementation of a bugged function.
Before generating the correct function, you should describe a bug and how to fix it in a natural language Python comment.
""".strip()

REFACT_SYSTEM_VERY_NEW_PROMPT = """
You're a bug fixing model. User will provide you a bugged python function and testcases function named "check". You need to generate a python file containing the corrected version of a python function. 
Before the correct function you need to reason why there is a bug in the function and how to correct it. The reasoning should be in a form of python comments.
Pay attention that you actually correct the function. Also pay attention to keeping all imports. The code must be able to compile.
Here is an example of your a conversation:

<empty_output>USER
from typing import List

def descending_sort(a: List[int]) -> List[int]:
    return sorted(a)

def check(descending_sort):
    assert descending_sort([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert descending_sort([1]) == [1]
    assert descending_sort([2, 5, 1, 9]) == [9, 5, 2, 1]

check(descending_sort)

Fix bugs in descending_sort
<empty_output>ASSISTANT
from typing import List

# the bug in descending_sort is that the sorting happens in a wrong order
# the sort should be in a descendent order, but the bugged function sorts the list in an ascending order
# to fix it we need to slice the array inversely after sorting
# here is the correct implementation
def descending_sort(a: List[int]) -> List[int]:
    return sorted(a)[::-1]
<empty_output><end of sequence>
""".strip()

CHECKER_CODE_TEMPLATE = """
from gen{id} import {function}

{testcases}
""".strip()
