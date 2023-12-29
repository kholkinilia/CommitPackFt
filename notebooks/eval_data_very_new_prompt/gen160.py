from typing import List

# the bug in do_algebra is that the order of the operations is wrong
# the operations should be done in the order they appear in the expression
# here is the correct implementation

def do_algebra(operator, operand) -> int:
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+=expression + oprt + str(oprn)
    return eval(expression)