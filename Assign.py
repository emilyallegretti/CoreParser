# Class corresponding to a Assign node in the abstract syntax tree.
from Error import printSyntaxError
from Expression import Expression
from Id import Id
from Scanner import Scanner
from Token import Token


class Assign: 
    def __init__(self):
        # initialize all children of Assign node
        self._id = None
        self._exp = None
    
    # Parse this Assign statement according to the BNF production.
    def parseAssign(self, tokens: Scanner):
        self._id = Id.parseId(tokens)
        # check if next token is an = sign
        if tokens.getToken() == Token.ASSIGN:
            # move to next token which should be an Expression
            tokens.skipToken()
            self._exp = Expression()
            self._exp.parseExpression(tokens)
            # check if last token is ;
            if tokens.getToken() == Token.SEMICOLON:
                return
        printSyntaxError('assignment')
        exit(1)


    
    # Print this Assign statement according to the BNF production.
    def printAssign(self):
        self._id.printId()
        print( " = ")
        self._exp.printExpression()
        print(";\n")
    
    # Execute this Assign statement.
    def evalAssign(self):
        result = self._exp.evalExpression
        # associate this Id node with the result of the assignment statement
        self._id.setIdVal(result)
        