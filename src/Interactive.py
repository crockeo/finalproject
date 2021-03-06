# Interactive.py

import Interpreter

def interactive():
    while (True):
        line = raw_input(": ")
        if (line == "quit"): break

        val = Interpreter.evaluate(line, False)
        if (val != 0): return val
