# Class corresponding to a CompOp node in the abstract syntax tree.
from Error import printError


class CompOp: 
    def __init__(self):
        # symbol will hold the terminal comparison operator corresponding to this instance
        self._symbol = None
    
    # Parse this CompOp statement according to the BNF production.
    def parseCompOp(self, tokens):
        tok = tokens.getToken()
        if tok == "!=":
            self._symbol = "!="
        elif tok == "==":
            self._symbol = "=="
        elif tok == "<":
            self._symbol = "<"
        elif tok == ">":
            self._symbol = ">"
        elif tok == "<=":
            self._symbol = "<="
        elif tok == ">=":
            self._symbol = ">="
        else:
            # if the current token is not one of the terminal production rules for CompOp, print error message and exit
            printError('comparison operator')
            exit(1)

        
    
    # Print this CompOp statement according to the BNF production.
    def printCompOp(self):
        print(self._symbol, end='')
