# Class corresponding to a Loop node in the abstract syntax tree.
from Condition import Condition
from Error import printSyntaxError
from PrettyPrint import TAB, printSpaces
from Scanner import Scanner
#from StatementSequence import StatementSequence
from Token import Token


class Loop: 
    def __init__(self):
        # initialize all possible children of Loop node
        self._cond = None
        self._ss = None
    
    # Parse this Loop statement according to the BNF production.
    def parseLoop(self, tokens: Scanner):
        # make sure current token is a While keyword
        if (tokens.getToken() == Token.WHILE.value):
            tokens.skipToken()      # go to next token which should be a Cond token
            self._cond = Condition()
            self._cond.parseCondition(tokens)
            # make sure next token is Loop keyword
            if tokens.getToken() == Token.LOOP.value:
                from StatementSequence import StatementSequence
                tokens.skipToken()  # go to next token which should be an SS token
                self._ss = StatementSequence()
                self._ss.parseStatementSequence(tokens)
                # make sure next 2 tokens are end and ;, otherwise syntax error
                if tokens.getToken() == Token.END.value:
                    tokens.skipToken()
                    if tokens.getToken() == Token.SEMICOLON.value:
                        tokens.skipToken()      # move cursor beyond end of statement
                        return

        printSyntaxError('loop')
        exit(1)

    
    # Pretty-print this Loop statement according to the BNF production.
    def printLoop(self,tabLevel):
        # print out the necessary amount of spaces to reach the current tab level
        printSpaces(tabLevel)
        print("while ", end="")
        self._cond.printCondition(); print("loop")
        tabLevel+=1
        self._ss.printStatementSequence(tabLevel)
        tabLevel = tabLevel-1
        printSpaces(tabLevel)
        print("end;")
    
    # Execute this Loop statement.
    def execLoop(self):
        while self._cond.evalCondition():
            self._ss.execStatementSequence()
        