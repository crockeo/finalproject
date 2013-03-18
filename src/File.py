# File.py

import Interpreter

def fload(path):
    f_read = open(path, "r")

    for line in f_read:
        val = Interpreter.evaluate(line)
        if val != 0: return val
