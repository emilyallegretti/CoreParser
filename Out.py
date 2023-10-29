# Class corresponding to a Out node in the abstract syntax tree.
from Declaration import Declaration
from Error import printRuntimeError, printSyntaxError
from IdList import IdList
from Scanner import Scanner
from Token import Token


class Out: 
    def __init__(self):
        # initialize child of Out
        self._idList = None
    
    # Parse this Out statement according to the BNF production.
    def parseOut(self, tokens:Scanner):
        # make sure first token is write keyword
        if tokens.getToken() == Token.WRITE:
            tokens.skipToken()
            self._idList = IdList()
            self._idList.parseIdList(tokens)
            # make sure final token is a semicolon
            if tokens.getToken()== Token.SEMICOLON:
                tokens.skipToken()
            return
        printSyntaxError('write')
        exit(1)


    
    # Print this Out statement according to the BNF production.
    def printOut(self):
        print("write ", end="")
        self._idList.printIdList()

    
    # Execute this Out statement.
    def execOut(self):
        # get the list of Id strings in idList and print each one out
        vars = self._idList.evalIdList()
        for var in vars:
            print(f"{var.name} = {var.evalId()}")