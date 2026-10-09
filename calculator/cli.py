from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand

# Path: read input -> choose the operation -> create a calculation
# -> create and execute a command -> print the answer.

def main():
    # converts the input into Operations.operation that belongs to 
    operations = {
    "add": Operations.add,
    "subtract": Operations.subtract,
    "multiply": Operations.multiply,
    "divide": Operations.divide,
    }

    history = [] 
    # empty history list

    while True:
        try:
            words = input("> ").split()
            # splits the input into individual --> seprates into "add 5 3" into ["add", "5", "3"]
        
        #  If input raises EOFError, stop. An empty line can simply start the next loop.
        except EOFError:
            break
        if not words:
            continue # asks for another command! 

        # the first word is exit, stop. If it is history, execute HistoryCommand 
        # and print its entries (or an empty-history message). 
        # These commands take no operands.
        if words[0] == "exit":
            break
        if words[0] == "history":
            entries = HistoryCommand(history).execute() # saves the entries to print them
        
            if entries: # prints the history entries in ENTRIES
                for entry in entries:
                    print(entry)
            else:
                print("History is empty.")

            continue

        # Otherwise, check that the name exists in the operation dictionary 
        # and that exactly two operands follow it.

        if words[0] not in operations:
            print("Unknown operation.")
            continue
        if len(words) != 3:
            print("Please enter an operation followed by two numbers.")
            continue

        try:
            # Convert the operands with float(). 
            a = float(words[1]) 
            b = float(words[2])
        except ValueError:
            # Catch ValueError for invalid numbers, 
            # show a message, and continue.
            print("Invalid numbers.")
            continue

        # Select the strategy, 
        operation = operations[words[0]]
        # use the class factory, 
        calculation = ArithmeticCalculation.create(a, b, operation) # calculation object has been created!
        # and build CalculateCommand. 
        label = " ".join(words) # remembers what the user types be rejoining the words 
        command = CalculateCommand(calculation, history, label) # create a command object that knows where to calculate and record a result
        # Execute it, print the answer, 
            # already happens in the try execpt loop! 
            # result = command.execute()
            # print(result)
        try: # attempt the calculation! 
            result = command.execute()
            print(result)
        except ValueError as error: # and catch ValueError for division by zero.
            print(error)

        # instructions:
        # Handle blank input, exit, and history.
        # Check the operation and operand count.
        # Convert the numbers, select the strategy, and build the pieces.
        # Execute the command and show its result or a helpful error.

'''
# removing the old test from step 4
calculation = ArithmeticCalculation.create(5, 3, Operations.add)
print(calculation.execute())  # 8
# testing the basic CLI structure

'''

