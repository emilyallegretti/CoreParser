# Class corresponding to a In node in the abstract syntax tree.
from Error import printRuntimeError, printSyntaxError
from IdList import IdList
from Token import Token
from Scanner import Scanner

class In: 
    data = None     # hold a static reference to the input data file
    def __init__(self):
        # initialize child node of In node
        self._idList = None
    
    # Parse this In statement according to the BNF production.
    def parseIn(self, tokens:Scanner):
        # make sure current token is a READ keyword
        if tokens.getToken()==Token.READ:
            tokens.skipToken()
            self._idList = IdList()
            self._idList.parseIdList()
            if tokens.getToken==Token.SEMICOLON:
                tokens.skipToken()
                return
        printSyntaxError("read")
        exit(1)
    
    # Print this In statement according to the BNF production.
    def printIn(self):
        print("read ", end="")
        self._idList.printIdList()
    
    # Execute this In statement by reading in the next line from the data file. If READ is executed with no data to read from 
    # the file, print runtime error and exit
    def execIn(self):
        # get a list of the ids contained in the id list
        ids = self._idList.evalIdList()
        # for each id in the id list, read a line from the data file and store its integer value in id
        # if EOF is reached during execution, abort with an error message
        for id in ids:
            line = In.data.readline()
            if line == "":
             printRuntimeError(f"No data in file to store in {id.name}")
             exit(1)
            else:
             id.setIdVal(int(line))

    # opens the given filename for reading and stores it in the data static variable.
    @staticmethod
    def openDataFile(filename):
        try:
            In.data = open(filename, "r")
        except FileNotFoundError as e:
            print(f"{e}.\nAborting program...")
            exit(1)
