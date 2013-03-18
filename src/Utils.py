# Utils.py

# Checking if a string is a proper number
def is_number(string):
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
