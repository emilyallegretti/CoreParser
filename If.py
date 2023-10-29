
# Class corresponding to an If node in the abstract syntax tree.
from Condition import Condition
from Error import printSyntaxError
from PrettyPrint import TAB, printSpaces
from Token import Token
class If: 
    def __init__(self):
        # initialize all possible children of an If node 
        self._cond = None
        self._ss1 = None
        self._ss2 = None
        # store the number corresponding to the alternator used, which will be set during parsing.
        self._altNo = None
    
    # Parse this If statement according to the BNF production.
    def parseIf(self, tokens):
        # make sure the current token is an If keyword
        if tokens.getToken() == Token.IF.value:
            tokens.skipToken()      # go to next token which should be a Cond node
            self._cond = Condition()
            self._cond.parseCondition(tokens)
            # make sure next token is a Then keyword
            if tokens.getToken() == Token.THEN.value:
                from StatementSequence import StatementSequence
                tokens.skipToken()  # go to next token which should be a Statement Sequence node
                self._ss1 = StatementSequence()
                self._ss1.parseStatementSequence(tokens)
                # if next token is 'end', we are in first alternate. if next token is 'else', we 
                # are in second alternate. otherwise, we have a syntax error
                if tokens.getToken() == Token.END.value:
                    tokens.skipToken()
                    # make sure the token that follows is a semicolon
                    if tokens.getToken() == Token.SEMICOLON.value:
                        self._altNo = 1     # store alternator number
                        tokens.skipToken()      # move cursor beyond end of statement
                        return
                elif tokens.getToken() == Token.ELSE.value:
                    tokens.skipToken()
                    # if this is an if-else stmt, parse ss2
                    self._ss2 = StatementSequence()
                    self._ss2.parseStatementSequence(tokens)
                    # make sure next 2 tokens are end and ;, otherwise syntax error
                    if tokens.getToken() == Token.END.value:
                        tokens.skipToken()
                        if tokens.getToken() == Token.SEMICOLON.value:
                            self._altNo = 2     # store alternator number
                            tokens.skipToken()      # move cursor beyond end of statement
                            return
        printSyntaxError("if")
        exit(1)

    
    # Pretty-print this If statement according to the BNF production.
    def printIf(self,tabLevel):
        # print out the necessary amount of spaces to reach the current tab level
        printSpaces(tabLevel)
        print("if ", end='')
        self._cond.printCondition()
        print('then')
        tabLevel=tabLevel+1
        self._ss1.printStatementSequence(tabLevel)
        tabLevel=tabLevel-1
        printSpaces(tabLevel)
        print("end;")
    
    # Execute this If statement.
    def execIf(self):
        if (self._cond.evalCondition()):
            self._ss1.execStatementSequence()
        elif(self._ss2):
            self._ss2.execStatementSequence()
        