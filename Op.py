# Class corresponding to a Op node in the abstract syntax tree.
from Error import printSyntaxError
from Id import Id
from Int import Int
from Scanner import Scanner
from Token import Token
from Expression import Expression

class Op: 
    def __init__(self):
        # the child node of this class will be dynamically initialized based on the alternative used.
        self._altNo = None
    
    # Parse this Op statement according to the BNF production.
    def parseOp(self, tokens: Scanner):
        t = tokens.getToken()
        if t== Token.NUMBER:
            # if current token is an int, create new Int object with its value 
            self._int = Int()
            self._int.parseInt()
            self._altNo  = 1
            return
        elif t==Token.ID:
            self._id = Id.parseId()
            self._altNo = 2
            return
        elif t==Token.OPEN_PAREN:
            tokens.skipToken()
            self._exp = Expression()
            self._exp.parseExpression()
            if tokens.getToken() == Token.CLOSED_PAREN:
                tokens.skipToken()
                self._altNo = 3
                return
        printSyntaxError("operand")
        exit(1)



    
    # Print this Op statement according to the BNF production.
    def printOp(self):
        if self._altNo == 1:
            self._int.printInt()
        elif self._altNo == 2:
            self._id.printId()
        else:
            print("(", end="")
            self._exp.printExpression()
            print(")")
    
    # Execute this Op statement.
    def evalOp(self):
        if self._altNo == 1:
            return self._int.evalInt()
        elif self._altNo == 2:
            return self._id.evalId()
        else:
            return self._exp.evalExpression()
        