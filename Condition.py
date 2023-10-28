# Class corresponding to a Condition node in the abstract syntax tree.
from Comp import Comp
from Error import printSyntaxError
from Scanner import Scanner
from Condition import Condition
from Token import Token


class Condition: 
    def __init__(self):
        # in this class, the children nodes will be dynamically set in the parse method based
        # on the alternate production rule being used, since each alternate has different child nodes.
        self._altNo = None
    
    # Parse this Condition statement according to the BNF production.
    def parseCondition(self, tokens: Scanner):
        tok = tokens.getToken()
        # if current token is an open paren, we are in first alternate <comp>
        if tok==Token.OPEN_PAREN:
            self._comp = Comp()
            self._comp.parseComp(tokens)
            self._altNo = 1
        # if current token is !, we are in second alternate !<comp>
        elif tok ==Token.NOT:
            tokens.skipToken()
            self._cond = Condition()
            self._cond.parseCondition(tokens)
            self._altNo = 2
        # if current token is open bracket, we are in third or fourth alternate
        elif tok ==Token.OPEN_BRACKET:
            tokens.skipToken()
            # parse first condition 
            self._cond1 = Condition()
            self._cond1.parseCondition(tokens)
            # check if this is conjuction or disjunction
            if tokens.getToken() == Token.AND:
                tokens.skipToken()
                self._cond2 = Condition()
                self._cond2.parseCondition(tokens)
                if tokens.getToken() == Token.CLOSE_BRACKET:
                    self._altNo = 3
                    tokens.skipToken()
                    return
            elif tokens.getToken() == Token.OR:
                tokens.skipToken()
                self._cond2 = Condition()
                self._cond2.parseCondition(tokens)
                if tokens.getToken() == Token.CLOSE_BRACKET:
                    self._altNo = 4
                    tokens.skipToken()
                    return
        printSyntaxError("condition")
        exit(1)




        
    
    # Print this Condition statement according to the BNF production.
    def printCondition(self):
        if self._altNo == 1:
            self._comp.printComp()
        elif self._altNo == 2:
            print("!",end="")
            self._cond.printCondition()
        elif self._altNo == 3:
            print("[", end="")
            self._cond1.printCondition()
            print("&&",end="")
            self._cond2.printCondition()
            print("]")
        else:
            print("[", end="")
            self._cond1.printCondition()
            print("||", end="")
            self._cond2.printCondition()
            print("]")
        
    
    # Evaluate this Condition statement based on the alternative number and return the Boolean result.
    def evalCondition(self):
        n = self._altNo
        if n==1:
            return self._comp.evalComp()
        elif n==2:
            return not(self._cond.evalCondition())
        elif n==3:
            return self._cond1.evalCondition() and self._cond2.evalCondition()
        else:
            return self._cond1.evalCondition() or self._cond2.evalCondition()
        