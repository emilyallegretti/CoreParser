# Class corresponding to a CompOp node in the abstract syntax tree.
from Error import printSyntaxError
from Token import Token


class CompOp: 
    def __init__(self):
        # symbol will hold the terminal comparison operator corresponding to this instance
        self.symbol = None
    
    # Parse this CompOp statement according to the BNF production.
    def parseCompOp(self, tokens):
        tok = tokens.getToken()
        if tok == Token.NOT_EQUALS.value:
            self.symbol = "!="
        elif tok == Token.EQUALS.value:
            self.symbol = "=="
        elif tok == Token.LESS_THAN.value:
            self.symbol = "<"
        elif tok == Token.GREATER_THAN.value:
            self.symbol = ">"
        elif tok == Token.LT_EQUALS.value:
            self.symbol = "<="
        elif tok == Token.GT_EQUALS.value:
            self.symbol = ">="
        else:
            # if the current token is not one of the terminal production rules for CompOp, print error message and exit
            printSyntaxError('comparison operator')
            exit(1)
        tokens.skipToken()

        
    
    # Print this CompOp statement according to the BNF production.
    def printCompOp(self):
        print(self.symbol, end='')
