# Class corresponding to a Id node in the abstract syntax tree.
from Error import *
from Scanner import Scanner
from Token import Token


class Id: 
    # static list that will hold the variables declared at the beginning of the program
    declaredVars = []
    def __init__(self, name: str):
        # each Id node must store its name (string) and assigned value (int)
        self.name = name
        self.value = None
        
    
    # Parse this Id statement by checking if it was declared in the declaration sequence, and returning it if so. If not, then abort program.
    @staticmethod
    def parseId(tokens: Scanner):
        # make sure current token is an Id, else we have a syntax error
        if tokens.getToken() == Token.ID:
            tokName = tokens.idName()
            if Id.isDeclared(tokName):
                for id in Id.declaredVars:
                    if id.name == tokName:
                        tokens.skipToken()
                        return id
            printUndeclaredError(tokName)
            exit(1)
        printSyntaxError("identifer")
        exit(1)
        
            

    # declare an Id by initializing it and adding it to declaredVars.
    # if the Id has already been declared, abort with an error message
    @staticmethod
    def declare(tokens:Scanner):
        # make sure current token is an Id token
        if tokens.getToken() == Token.ID:
            # get the name of the Id token
            tokName = tokens.idName()
            # check if Id name is already declared. if not, create new Id and add it to declaredVars
            if Id.isDeclared(tokName):
                printDoubleDeclError(tokName)
                exit(1)
            else:
                id = Id(tokName)
                Id.declaredVars.append(id)
                tokens.skipToken()
                return id
        printSyntaxError("identifier")
            
            


    
    # Print this Id statement according to the BNF production.
    def printId(self):
        print(self.name)
    
    # Evaluate this Id statement by returning the value assigned to it. If it is uninitialized, print an error message and abort
    def evalId(self):
        if self.value == None:
            printRuntimeError(f"{self.name} has not been initialized")
        else: 
            return self.value
        
    # Sets the value of this Id object to given val.
    def setIdVal(self, val):
        self.value = val

# checks the declaredVars list to see if the given idName is already used by an existing variable. returns true if so, false otherwise.
    @staticmethod
    def isDeclared(idName: str):
        # check if one of the Ids in declaredVars already has that name, if so print error and exit
        for id in Id.declaredVars:
            if id.name() == idName:
                return True
        return False
