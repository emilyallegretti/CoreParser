# Class corresponding to a Declaration node in the abstract syntax tree.
from Error import printSyntaxError
from Id import Id
from IdList import IdList
from Token import Token


class Declaration:
    # initialize a static list of variables declared by the program 
    declaredVars = []

    def __init__(self):
        # initialize child of Declaration node
        self._idList = None
       

    
    # Parse this Declaration statement according to the BNF production.
    def parseDeclaration(self, tokens):
        # make sure current token is int keyword
        if tokens.getToken() == Token.INT:
            tokens.skipToken()
            self._idList = IdList()
            # initialize the variables declared here and abort with an error if a double declaration occurs. 
            self._idList.declareIdList()
            if tokens.getToken()==Token.SEMICOLON:
                tokens.skipToken()
                return
        printSyntaxError("declaration")
        exit(1)
    
    # Print this Declaration statement according to the BNF production.
    def printDeclaration(self):
        print("int ", end="")
        self._idList.printIdList()
        print(";")
    
    # Execute this Declaration statement by adding each variable in the idList to a static list of declared variables, which will be used
    # by the parser to check if future Id instances were declared by the program
    def execDeclaration(self):
         vars = self._idList.evalIdList()
        