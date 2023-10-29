import sys
from In import In
from Program import Program
from Scanner import Scanner

# Main driver method that will trigger the recursive descent parser, printer, and executor.
def main(args):
    # create a Scanner instance that will tokenize the input program and allow the parser to access tokens
    tokens=Scanner(args[1])      # first CL arg is the name of the input file
    # create root node of abstract parse tree corresponding to input program
    prog = Program()
    # first parse the input program
    print("------------------PARSING PROGRAM---------------------")
    prog.parseProgram(tokens)
    # then pretty-print it
    print("------------------PRINTING PROGRAM---------------------")
    prog.printProgram()
    # finally, execute the program
    # first, open the data file as a static variable of the In class
    In.openDataFile(args[2])     # second command-line argument is the name of the data file to read from
    print("------------------EXECUTING PROGRAM---------------------")
    prog.execProgram()

main(sys.argv)