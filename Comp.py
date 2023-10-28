from Error import printSyntaxError
# Class corresponding to a Comp node in the abstract syntax tree.
from CompOp import CompOp
from Op import Op
from Scanner import Scanner
from Token import Token


class Comp: 
    def __init__(self):
        # initialize all children of Comp node
        self._op1 = None
        self._compOp = None
        self._op2 = None
    
    # Parse this Comp statement according to the BNF production.
    def parseComp(self, tokens: Scanner):
        # make sure first token is (
        if tokens.getToken() == Token.OPEN_PAREN:
            tokens.skipToken()  # go to next token which should be an Op node
            self._op1 = Op()
            self._op1.parseOp(tokens)
            # next token should be CompOp node
            self._compOp = CompOp()
            self.compOp.parseCompOp(tokens)
            # next token should be Op node
            self._op2= Op()
            self._op2.parseOp()
            # check last token is )
            if tokens.getToken() == Token.CLOSE_PAREN:
                tokens.skipToken()      # move cursor beyond end of statement
                return
        # if we reach this point in the code, we have a syntax error
        printSyntaxError("comparison")
        exit(1)

    
    # Print this Comp statement according to the BNF production.
    def printComp(self):
        print("("); 
        self._op1.printOp(); 
        print(" ")
        self._compOp.printCompOp(); 
        print(" ")
        self._op2.printOp()
        print(")\n")
    
    # Exthis Comp statement.
    def evalComp(self):
        # get the symbol associated with the compOp node's alternate
        symbol = self._compOp.symbol
        res1 = self._op1.evalOp()
        res2 = self._op2.evalOp()
        # evaluate the comparison statement based on the symbol 
        if symbol == "!=":
            return not(res1 == res2)
        elif symbol == "==":
            return res1==res2
        elif symbol == "<":
            return res1 < res2
        elif symbol == ">":
            return res1>res2
        elif symbol == "<=":
            return res1<=res2
        elif symbol == ">=":
            return res1>=res2

        