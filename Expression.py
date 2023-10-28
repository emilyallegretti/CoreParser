# Class corresponding to a Expression node in the abstract syntax tree.
from Fac import Fac
from Scanner import Scanner
from Token import Token


class Expression: 
    def __init__(self):
        #initialize all possible children of Expression
        self._fac = None
        self._exp = None
        self._altNo = None
    
    # Parse this Expression statement according to the BNF production.
    def parseExpression(self, tokens: Scanner):
        # in either alternative, <fac> is the first token to be parsed
        self._fac = Fac()
        self._fac.parseFac()
        self._altNo = 1
        # if next token is a + or - token, we are in second/third alternative
        if tokens.getToken() == Token.PLUS:
            self._altNo = 2
            tokens.skipToken()
            self._exp = Expression()
            self._exp.parseExpression(tokens)
        elif tokens.getToken() == Token.MINUS:
            self._altNo = 3 
            tokens.skipToken()
            self._exp = Expression()
            self._exp.parseExpression(tokens)
        
    
    # Print this Expression statement according to the BNF production.
    def printExpression(self):
        self._fac.printFac()
        if self._altNo > 1:
            if self._altNo == 2:
                print(" + ")
            elif self._altNo == 3:
                print(" - ")
            self._exp.printExpression()

    
    # Evaluate this Expression statement and return the numeric result.
    def evalExpression(self):
        if self._altNo == 1:
            return self._fac.evalFac()
        elif self._altNo == 2:
            return self._fac.evalFac() + self._exp.evalExpression()
        else:
            return self._fac.evalFac() - self._exp.evalExpression()
        