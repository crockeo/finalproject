# IfElse.py

import Interpreter
import Utils

# Performing an operation
def _do_op(n1, o1, n2):
    if o1 == "==": return n1 == n2
    elif o1 == "!=": return n1 != n2
    elif o1 == "&&": return Utils.to_boolean(n1) and Utils.to_boolean(n2)
    elif o1 == "||": return Utils.to_boolean(n1) or Utils.to_boolean(n2)

# Checking if an operator is a boolean operator
def _is_boolean_operator(operator): return operator == "==" or operator == "!=" or operator == "&&" or operator == "||"

# Checking the beginning of where a boolean statement is
def get_start_of_boolean(sline):
    for x in range(0, len(sline) - 2):
        if Utils.is_number(sline[x]) and _is_boolean_operator(sline[x + 1]) and Utils.is_number(sline[x + 2]):
            return x
    return False

# Finding if an sline has a boolean expression
def has_boolean_expression(sline):
    if get_start_of_boolean(sline) == False: return False
    return True

# Evaluating the boolean expressions in the sline
def do_boolean_expressions(sline):
    while True:
        pos = get_start_of_boolean(sline)
        if pos == False: break

        sline.insert(pos, _do_op(sline.pop(pos), sline.pop(pos), sline.pop(pos)))
    return sline

# Performing an if statement
def perform_block_statement(lines, mode):
    for x in lines:
        Interpreter.evaluate(x, mode)
