# Class corresponding to a DeclarationSequence node in the abstract syntax tree.
from Declaration import Declaration
from Error import printSyntaxError
from Scanner import Scanner
from Token import Token


class DeclarationSequence: 
    def __init__(self):
        #initialize all posisble children of Declaration Sequence node
        self._decl = None
        self._declSeq = None
    
    # Parse this DeclarationSequence statement according to the BNF production.
    def parseDeclarationSequence(self, tokens: Scanner):
        self._decl = Declaration()
        self._decl.parseDeclaration(tokens)
        # check if next token is an INT keyword; this indicates we are in second alternative of prod. rule
        if tokens.getToken() == Token.INT.value:
            self._declSeq = DeclarationSequence()
            self._declSeq.parseDeclarationSequence(tokens)

    
    # Print this DeclarationSequence statement according to the BNF production.
    def printDeclarationSequence(self,tabLevel):
        self._decl.printDeclaration(tabLevel)
        if self._declSeq:
            self._declSeq.printDeclarationSequence(tabLevel)
    
    # Execute this Declaration Sequence statement.
    def execDeclarationSequence(self):
        self._decl.execDeclaration()
        if self._declSeq:
            self._declSeq.execDeclarationSequence()
        