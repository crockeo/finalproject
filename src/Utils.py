# Utils.py

# Checking if a string is a proper number
def is_number(string):
    if isinstance(string, (int, long)): return True
    
    try:
        int(string)
        return True
    except ValueError:
        return False

# Converting a value to a boolean
def to_boolean(value):
    if not (type(value) is int): return False
    if (value == 0): return False
    return True
