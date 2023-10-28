# Class corresponding to a Loop node in the abstract syntax tree.
from Condition import Condition
from Error import printSyntaxError
from Scanner import Scanner
from StatementSequence import StatementSequence
from Token import Token


class Loop: 
    def __init__(self):
        # initialize all possible children of Loop node
        self._cond = None
        self._ss = None
    
    # Parse this Loop statement according to the BNF production.
    def parseLoop(self, tokens: Scanner):
        # make sure current token is a While keyword
        if (tokens.getToken() == Token.WHILE):
            tokens.skipToken()      # go to next token which should be a Cond token
            self._cond = Condition()
            self._cond.parseCondition()
            # make sure next token is Loop keyword
            if tokens.getToken() == Token.LOOP:
                tokens.skipToken()  # go to next token which should be an SS token
                self._ss = StatementSequence()
                self._ss.parseStatementSequence()
                # make sure next 2 tokens are end and ;, otherwise syntax error
                if tokens.getToken() == Token.END:
                    tokens.skipToken()
                    if tokens.getToken() == Token.SEMICOLON:
                        tokens.skipToken()      # move cursor beyond end of statement
                        return

        printSyntaxError('loop')
        exit(1)

    
    # Pretty-print this Loop statement according to the BNF production.
    def printLoop(self):
        print("while ")
        self._cond.printCondition(); print("loop\n\t")
        self._ss.printStatementSequence(); print("end;\n")
    
    # Execute this Loop statement.
    def evalLoop(self):
        while self._cond.evalCondition():
            self._ss.execStatementSequence()
        