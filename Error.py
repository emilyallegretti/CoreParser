# This module provides a single method that prints out a syntax error message corresponding to the given Core statement.

def printError(type: str):
    print(f"Syntax error in {type.upper()} statement. Aborting program...")