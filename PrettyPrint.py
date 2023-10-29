# This module includes standards used for pretty-printing a program: a constant TAB value, which defines the tab size used in this program
#(4 spaces), as well as a printSpaces function that will print a sequential amount of tabs given an indentLevel.


# Constant for amount of spaces in a 'tab', used for pretty-printing the program
TAB = "    "

# given an indent level, prints TAB*indentlevel spaces.
def printSpaces(indentLevel):
    for _ in range(indentLevel):
        print(TAB, end="")
