# Class corresponding to a Op node in the abstract syntax tree.
from Scanner import Scanner
from Token import Token

class Op: 
    def __init__(self):
        # the child node of this class will be dynamically initialized based on the alternative used.
        self._altNo = None
    
    # Parse this Op statement according to the BNF production.
    def parseOp(self, tokens: Scanner):
        if tokens.getToken() == Token.NUMBER:
            None

    
    # Print this Op statement according to the BNF production.
    def printOp(self):
        None
    
    # Execute this Op statement.
    def evalOp(self):
        None
        