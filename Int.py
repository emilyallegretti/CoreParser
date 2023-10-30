# Class corresponding to a Int node in the abstract syntax tree.
from Error import printSyntaxError
from Scanner import Scanner
from Token import Token


class Int: 
    def __init__(self):
        self._value = None
    
    # Parse this Int statement by .
    def parseInt(self, tokens: Scanner):
        # make sure current token is an int
        if tokens.getToken() == Token.NUMBER.value:
            self._value = tokens.intVal()
            tokens.skipToken()
        else:
            printSyntaxError("integer")
            exit(1)
    
    # Print this Int statement according to the BNF production.
    def printInt(self):
        print(self._value,end="")
    
    # Evaluate this Int statement by returning its numeric value.
    def evalInt(self):
        return self._value
        