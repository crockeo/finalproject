# Interpreter.py

import ProgramState
import Utils

import Print
import Variable
import Arithmetic
import IfElse

####
# General Functions
#

# Converting every variable into its value equivilent
def _convert_to_values(start, sline):
    for x in range(start, len(sline)):
        if ProgramState.var_exists(sline[x]):
            sline[x] = ProgramState.get_variable(sline[x])
        elif Utils.is_number(sline[x]):
            sline[x] = int(sline[x])
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
#
def _has_arithmetic_statement(sline): return Arithmetic.has_arithmetic_statement(sline)

####
# If/Else
#
def _is_start_bracket(sline): return len(sline) == 1 and sline[0] == "{"
def _is_end_bracket(sline): return len(sline) == 1 and sline[0] == "}"

def _is_if_statement(sline): return len(sline) == 2 and sline[0] == "if" and isinstance(sline[1], bool)
def _is_if_statement_true(sline): return _is_if_statement(sline) and sline[1] == True

def _is_else_if_statement(sline): return len(sline) == 3 and sline[0] == "else" and sline[1] == "if" and isinstance(sline[2], bool)
def _is_else_if_statement_true(sline, ss): return _is_else_if_statement(sline) and sline[2] == True and (not ss)

def _is_else_statement(sline): return len(sline) == 1 and sline[0] == "else"
def _is_else_statement_true(sline, ss): return _is_else_statement(sline) and (not ss)

####
# Evaluation
#

# Checking for the if/else block ending
_do_block = False
_looking_for_end_bracket   = False
_record_lines = False
_lines = []
_same_string = False

# Note - mode states:
#  False - Interactive
#  True  - File Loading
def evaluate(line, mode):
    global _do_block
    global _looking_for_end_bracket
    global _record_lines
    global _lines
    global _same_string

    if line == "quit": return 1
    sline = line.split(" ")

    sline = _convert_to_values(1, sline)
    sline = Arithmetic.do_arithmetic_statements(sline)
    sline = IfElse.do_boolean_expressions(sline)

    # Checking if the line is both from a file and an if statement
    if mode:
        if _is_if_statement_true(sline) or _is_else_if_statement_true(sline, _same_string) or _is_else_statement_true(sline, _same_string):
            _do_block = True
            _same_string = True
        elif _is_start_bracket(sline):
            _record_lines = True
            _looking_for_end_bracket = True
        elif _looking_for_end_bracket and _is_end_bracket(sline):
            _record_lines = False
            _looking_for_end_bracket = False
            if _do_block: IfElse.perform_block_statement(_lines, mode)
            _lines = []
            _do_block = False
        elif _record_lines:
            _lines.append(line)
            return 0
        elif _is_else_if_statement(sline) or _is_else_statement(sline) or _do_block:
            pass
        else:
            _same_string = False

    # Checking if the line is a variable set statement
    if _is_variable_set_statement(sline):
        val = Variable.variable_set_statement(sline)
        if val: return val

    # Checking if the line is a print statement
    if _is_print_statement(sline):
        val = Print.print_statement(sline)
        if val: return val
    
    return 0
    evaluate_sline(line.split(" "), mode)