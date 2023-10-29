# This module provides methods that prints out different types error messages depending on the phase the interpreter is in (i.e.
# parsing, printing, executing) .

def printSyntaxError(type: str):
    print(f"Syntax error in {type.upper()} statement. Aborting program...")

def printRuntimeError(error: str):
    print (f"Runtime error: {error}. Aborting program...")

def printDoubleDeclError(varName: str):
    print(f"Parser Error: {varName} has already been declared. Aborting program...")

def printUndeclaredError(varName: str):
    print(f"Parser Error: {varName} has not been declared. Aborting program... ")



