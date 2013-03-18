# Interpreter.py

import ProgramState
import Utils

import Print
import Variable
import Arithmetic
import IfElse
import While
import For

####
# General Functions
#

# Converting every variable into its value equivilent
def _convert_to_values(start, sline):
    for x in range(start, len(sline)):
        if ProgramState.var_exists(sline[x]):
            sline[x] = ProgramState.get_variable(sline[x])
    return sline

####
# Printing
# 
def _is_print_statement(sline):
    if len(sline) == 2 and sline[0] == "print" and (Utils.is_number(sline[1]) or ProgramState.var_exists(sline[1])):
        return True
    return False

####
# Variables
# 
def _is_variable_set_statement(sline):
    if len(sline) == 3 and ProgramState.var_is_proper(sline[0]) and (Utils.is_number(sline[2]) or ProgramState.var_exists(sline[2])):
        return True
    return False

####
# Arithmetic
#  Nothing to see here!
#
def _has_arithmetic_statement(sline): return Arithmetic.has_arithmetic_statement(sline)

####
# If/Else
# TODO
def _is_if_statement(sline):
    pass

def _is_else_statement(sline):
    pass

def _is_else_if_statement(sline):
    pass

####
# While
# TODO
def _is_while_statement(sline):
    pass

####
# For
# TODO
def _is_for_statement(sline):
    pass

####
# Evaluation
#

# Note - mode states:
#  False - Interactive
#  True  - File Loading
def evaluate(line, mode):
    sline = line.split(" ")

    sline = _convert_to_values(1, sline)
    sline = Arithmetic.do_arithmetic_statements(sline)

    # Checking if the line is a variable set statement
    if _is_variable_set_statement(sline):
        val = Variable.variable_set_statement(sline)
        if val: return val

    # Checking if the line is a print statement
    if _is_print_statement(sline):
        val = Print.print_statement(sline)
        if val: return val

    if mode:
        pass
    
    return 0
