# Class corresponding to a Program node in the abstract syntax tree.
from Error import printSyntaxError
from Scanner import Scanner
from Token import Token
from DeclarationSequence import DeclarationSequence
from StatementSequence import StatementSequence


class Program: 
    # initialize all possible children of the Program node
    def __init__(self):
        self._ds = None
        self._ss = None
    
    # Parse this Program statement according to the BNF production.
    def parseProgram(self, tokens:Scanner):
        # make sure current token is a program keyword
        if tokens.getToken() == Token.PROGRAM:
            tokens.skipToken()
            self._ds = DeclarationSequence()
            self._ds.parseDeclarationSequence(tokens)
            if tokens.getToken() == Token.BEGIN:
                tokens.skipToken()
                self._ss = StatementSequence()
                self._ss.parseStatementSequence(tokens)
                if tokens.getToken() == Token.END:
                    tokens.skipToken()
                    return
        # if we've reached this point in the code, we have a syntax error--print error message and quit
        printSyntaxError('program')
        exit(1)
    
    # Print this Program statement according to the BNF production.
    def printProgram(self):
        print("program ", end="")
        self._ds.printDeclarationSequence()
        print("begin ", end="")
        self._ss.printStatementSequence()
        print("end")

    
    # Execute this Program statement.
    def execProgram(self):
       # no need to 'execute' the declaration sequence, since variable declaration was handled during parsing
        # execute the statement sequence that follows, passing the data file along
        self._ss.executeStatementSequence()
        