# ProgramState.py

_variables = {}

def set_variable(name, val): _variables[name] = val
def var_exists(name): return (name in _variables)
def var_is_proper(name): return (isinstance(name, basestring) and name[0] == "$")
def var_exists_and_is_proper(name): return (var_is_proper(name) and var_exists(name))
def get_variable(name):
    if not var_exists(name): return False
    else: return _variables[name]
