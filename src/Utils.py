# Utils.py

# Checking if a string is a proper number
def is_number(string):
    if isinstance(string, (int, long)): return True
    
    try:
        int(string)
        return True
    except ValueError:
        return False

# Checking if a string is a proper boolean
def is_boolean(value):
    if value == "True" or value == "False" or isinstance(value, bool): return True
    return False

# Converting a value to a boolean
def to_boolean(value):
    if isinstance(value, int):
        if value == 0: return False
        return True
    elif isinstance(value, str):
        if value == "False": return False
        return True
    elif isinstance(value, bool): return value
    else: return False
