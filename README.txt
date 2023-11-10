Core Parser, Printer, Executor Project
By Emily Allegretti

***USAGE***
Prerequisites:
Latest version of python3 installed on your machine

To run the Core Parser, Printer, Executor
1. Download and unzip the project folder
2. From the command line, cd into unzipped project folder
3. Run this command:
    python3 PPEMain.py <input_prog> <data_file>
    where <input_prog> is the input Program that is to be tokenized, parsed, printed, and executed, and <data_file> is a CORRECTLY-FORMATTED data file,
    consisting of one integer on each line that will be read during execution whenever 'read' statements are encountered.   

***OVERVIEW***
This program is the interpreter for the Core language, which consists of a parser, printer, and executor, as well as the 
Core Tokenizer. 
Given an input program file and a data file from the command line, the main function will first construct 
an instance of Scanner (Scanner.py), passing in the input program, which will "scan" each line in the input file into a 
an array of valid tokens that can be accessed during parsing with getToken() and skipToken() functions. This means that if invalid tokens according
to the Core DFA are encountered in the input program, this will be found by the Scanner, and the program will be aborted during scanning/parsing. 

The main function will then construct an abstract syntax tree (AST) of the input program by first constructing an instance of Program, which is the root node and first production rule of 
any Core program according to the BNF, and then calling the Program object's parseProgram() function. This will trigger a recursive-descent-parsing of the entire input program, recursively constructing the AST. 
This means that if any syntax errors or doubly-declared variables in the top-level declaration sequence are encountered in the input program, 
this will be found by the Parser, and the program will be aborted during parsing.

After the AST is constructed during recursive-descent parsing and no syntax errors are found, the main function will then call Program's printProgram() function, which will similarly
pretty-print the input program in a recursive-descent manner by starting at the root program node. In the context of this project, 'pretty-printing' 
means that the program will be printed using Python indentation style.

Finally, the main function will call the Program object's executeProgram() function, which will similarly trigger a recursive-descent execution of the program, starting at the 
root Program node. The Executor will either interpet statements, or evaluate statements and return a result, based on the statement's purpose.
For example, 'if' statements will be executed based on the condition given, but 'expression' statements will be evaluated, returning the result of
the expression to the calling function. The executor will handle context-sensitive runtime requirements such as uninitialized variables and 'read' statements
that do not find a corresponding value to be read in the data file.

