# Class corresponding to a Program node in the abstract syntax tree.
from Error import printSyntaxError
from PrettyPrint import TAB
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
        if tokens.getToken() == Token.PROGRAM.value:
            tokens.skipToken()
            self._ds = DeclarationSequence()
            self._ds.parseDeclarationSequence(tokens)
            if tokens.getToken() == Token.BEGIN.value:
                tokens.skipToken()
                self._ss = StatementSequence()
                self._ss.parseStatementSequence(tokens)
                if tokens.getToken() == Token.END.value:
                    tokens.skipToken()
                    return
        # if we've reached this point in the code, we have a syntax error--print error message and quit
        printSyntaxError('program')
        exit(1)
    
    # Pretty-print this Program statement according to the BNF production.
    def printProgram(self):
        print("program")
        tabLevel = 1  # set tab level that decl seq will be at
        self._ds.printDeclarationSequence(tabLevel)
        print(f"{TAB}begin")
        tabLevel += 1     # set tab level that statement seq will be at
        self._ss.printStatementSequence(tabLevel)
        print("\nend")

    
    # Execute this Program statement.
    def execProgram(self):
       # no need to 'execute' the declaration sequence, since variable declaration was handled during parsing
        # execute the statement sequence that follows, passing the data file along
        self._ss.execStatementSequence()
        