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
def _is_equality_operator(operator): return operator == "==" or operator == "!="
def _is_and_operator(operator): return operator == "&&" or operator == "||"
def _is_boolean_operator(operator): return _is_equality_operator(operator) or _is_and_operator(operator)

# Getting the start of an equality statement
def _get_start_of_equality(sline):
    for x in range(0, len(sline) - 2):
        if Utils.is_number(sline[x]) and _is_equality_operator(sline[x + 1]) and Utils.is_number(sline[x + 2]):
            return x
    return False

# Getting the start of an and (or 'or') statement
def _get_start_of_and(sline):
    for x in range(0, len(sline) - 2):
        if Utils.is_number(sline[x]) and _is_and_operator(sline[x + 1]) and Utils.is_number(sline[x + 2]):
            return x
    return False


def get_start_of_boolean(sline):
    for x in range(0, len(sline) - 2):
        if Utils.is_number(sline[x]) and _is_boolean_operator(sline[x + 1]) and Utils.is_number(sline[x + 2]):
            return x
    return False

# Finding if an sline has a boolean expression
def has_boolean_expression(sline):
    if get_start_of_boolean(sline) == False: return False
    return True

# Doing all == and != operations
def _do_all_equality_operations(sline):
    while True:
        pos = _get_start_of_equality(sline)
        if pos == False: break

        sline.insert(pos, _do_op(sline.pop(pos), sline.pop(pos), sline.pop(pos)))
    return sline

# Doing all && and || operations
def _do_all_and_operations(sline):
    while True:
        pos = _get_start_of_and(sline)
        if pos == False: break

        sline.insert(pos, _do_op(sline.pop(pos), sline.pop(pos), sline.pop(pos)))
    return sline

# Evaluating the boolean expressions in the sline
def do_boolean_expressions(sline): return _do_all_and_operations(_do_all_equality_operations(sline))

# Performing an if statement
def perform_block_statement(lines, mode):
    for x in lines:
        Interpreter.evaluate(x, mode)
