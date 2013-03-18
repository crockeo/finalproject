# Variable.py

import ProgramState
import Utils

# Setting variables
def variable_set_statement(sline):
    if ProgramState.var_is_proper(sline[2]):
        if ProgramState.var_exists(sline[2]): ProgramState.set_variable(sline[0], sline[2])
        else: return 1
    elif Utils.is_number(sline[2]): ProgramState.set_variable(sline[0], int(sline[2]))
    else: return 1

    return 0
