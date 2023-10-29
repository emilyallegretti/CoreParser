# Class corresponding to a Fac node in the abstract syntax tree.
from Op import Op
from Scanner import Scanner
from Token import Token


class Fac: 
    def __init__(self):
        #initialize all possible children of Fac node
        self._op = None
        self._fac = None
    
    # Parse this Fac statement according to the BNF production.
    def parseFac(self, tokens:Scanner):
        self._op = Op()
        self._op.parseOp(tokens)
        if tokens.getToken == Token.ASTERISK.value:
            tokens.skipToken()
            self._fac = Fac()
            self._fac.parseFac(tokens)
    
    # Print this Fac statement according to the BNF production.
    def printFac(self):
        self._op.printOp()
        if self._fac:
            print(" * ", end="")
            self._fac.printFac()
    
    # Execute this Fac statement.
    def evalFac(self):
        if self._fac:
            return self._op.evalOp() * self._fac.evalFac()
        else:
            return self._op.evalOp()
        