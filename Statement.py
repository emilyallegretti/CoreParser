# Class corresponding to a Statement node in the abstract syntax tree.
from Assign import Assign
from If import If
from In import In
from Loop import Loop
from Out import Out
from Scanner import Scanner
from Token import Token


class Statement: 
    def __init__(self):
        self._altNo = None
        # child of this Statement node will be typecasted to the correct object based on the alternator type used.
        self._child = None
    
    # Parse this Statement statement according to the BNF production.
    def parseStatement(self, tokens:Scanner):
        t = tokens.getToken()
        # check what alternative this Statement is in
        if t==Token.ID:
            self._altNo = 1
            self._child = Assign()
            self._child.parseAssign(tokens)
            return
        elif t==Token.IF:
            self._altNo = 2
            self._child = If()
            self._child.parseIf(tokens)
        elif t==Token.WHILE:
            self._altNo = 3
            self._child = Loop()
            self._child.parseLoop(tokens)
        elif t==Token.READ:
            self._altNo = 4
            self._child = In()
            self._child.parseIn(tokens)
        elif t==Token.WRITE:
            self._altNo = 5
            self._child = Out()
            self._child.parseOut(tokens)
    
    # Print this Statement statement according to the BNF production.
    def printStatement(self):
        a = self._altNo
        if a==1:
            self._child.printAssign()
        elif a==2:
            self._child.printIf()
        elif a==3:
            self._child.printLoop()
        elif a==4:
            self._child.printIn()
        elif a==5:
            self._child.printOut()
    
    # Execute this Statement.
    def execStatement(self):
        a = self._altNo
        if a == 1:
            self._child.execAssign()
        elif a == 2:
            self._child.execIf()
        elif a == 3:
            self._child.execLoop()
        elif a == 4:
            self._child.execIn()
        elif a == 5:
            self._child.execOut()
        