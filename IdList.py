# Class corresponding to a IdList node in the abstract syntax tree.
from Id import Id
from Scanner import Scanner
from Token import Token


class IdList: 
    def __init__(self):
        #initialize all possible children of IdList
        self._id = None
        self._idList = None
    
    # Parse this IdList statement according to the BNF production. This function will be called when parsing the statement sequence 
    # portion of the program. 
    def parseIdList(self, tokens: Scanner):
        self._id = Id.parseId(tokens)
        # if next token is a comma, then we are in second alternative
        if tokens.getToken() == Token.COMMA.value:
            tokens.skipToken()
            self._idList = IdList()
            self._idList.parseIdList(tokens)
    
    # This function will be called when parsing the declaration sequence portion of the program. Initialize each Id declared in the Id list.
    def declareIdList(self, tokens:Scanner):
        self._id = Id.declare(tokens)
        # check if we are in second alternative
        if tokens.getToken() == Token.COMMA.value:
            tokens.skipToken()
            self._idList = IdList()
            self._idList.declareIdList(tokens)
    
    # Print this IdList statement according to the BNF production.
    def printIdList(self):
        self._id.printId()
        if self._idList:
            print(", ", end="")
            self._idList.printIdList()

    
    # Evaluate this IdList statement by returning a list of the Ids it contains. 
    def evalIdList(self):
        ids = [self._id]
        if self._idList:
            ids2 = self._idList.evalIdList()
            for id in ids2:
                ids.append(id)
        return ids
        
        