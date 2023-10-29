# Class corresponding to a StatementSequence node in the abstract syntax tree.
from Scanner import Scanner
from Statement import Statement
from Token import Token


class StatementSequence: 
    def __init__(self):
        # initialize all possible children of stmt seq
        self._stmt = None
        self._ss = None
    
    # Parse this StatementSequence statement according to the BNF production.
    def parseStatementSequence(self, tokens:Scanner):
        self._stmt = Statement()
        self._stmt.parseStatement(tokens)
        # check if next token is the start of another Statement Sequence, this indicates we are in second alternative
        t = tokens.getToken()
        if t == Token.ID.value or t==Token.IF.value or t==Token.WHILE.value or t==Token.READ.value or t==Token.WRITE.value:
            self._ss = StatementSequence()
            self._ss.parseStatementSequence(tokens)
    
    # Print this StatementSequence statement according to the BNF production.
    def printStatementSequence(self, tabLevel):
        self._stmt.printStatement(tabLevel)
        if self._ss:
            self._ss.printStatementSequence(tabLevel)

    
    # Execute this StatementSequence statement.
    def execStatementSequence(self):
        self._stmt.execStatement()
        if self._ss:
            self._ss.execStatementSequence()
        