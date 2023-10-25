from Scanner import Scanner

# global variable for a Scanner instance, which will tokenize the input program and allow the parser to iterate through tokens.
t=None

# Main driver method that will trigger the recursive descent parser, printer, and executor.
def main(args):
    # instantiate t
    t=Scanner(args[1])      # first CL arg is the name of the input file
    # create root node of abstract parse tree corresponding to input program
    prog = Program()
    # first parse the input program
    prog.parseProgram()
    # then pretty-print it
    prog.printProgram()
    # finally, execute the program using the second CL arg, which is the data file
    try:
        data = open(args[2], 'r')
    except FileNotFoundError as e:
        print(f"{e}.\nAborting program...")
        exit(1)
#TODO: should data file also be a global variable among all print methods?
    prog.execProgram(data)