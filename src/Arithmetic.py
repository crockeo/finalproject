# Arithmetic.py

import Utils

# Checking if a specific string is an operator
def _is_operator(string): return (string == "+" or string == "-" or string == "*" or string == "/")

# Doing a single operation
def _do_op(n1, o1, n2):
    if not _is_operator(o1): return False
    if not (Utils.is_number(n1) and Utils.is_number(n2)): return False

    if o1 == "+": return int(n1) + int(n2)
    elif o1 == "-": return int(n1) - int(n2)
    elif o1 == "*": return int(n1) * int(n2)
    elif o1 == "/": return int(int(n1) / int(n2)) 

# Getting the index of the start of an arithmetic operation
def get_start_of_arithmetic(sline):
    for x in range(0, len(sline) - 2):
        if Utils.is_number(sline[x]) and _is_operator(sline[x + 1]) and Utils.is_number(sline[x + 2]):
            return x
    return False

# Checking if a line still has an arithmetic statement
def has_arithmetic_statement(sline):
    if get_start_of_arithmetic(sline) != False: return True
    return False

# Simplifying the statement
def do_arithmetic_statements(sline):
    val = get_start_of_arithmetic(sline)
    while val != False:
        sline.insert(val, _do_op(sline.pop(val), sline.pop(val), sline.pop(val)))

        val = get_start_of_arithmetic(sline)

    return sline
