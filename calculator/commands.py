from calculator.calculation import Calculation

# a COMMAND is an object that represents an ACTION

class CalculateCommand:
    def __init__(self, calculation: Calculation, history: list[str], label: str):
        # The command receives its pieces instead of building them.
        self.calculation = calculation
        # calculation: Calculation in the parameters MEANS calculation is a Calculation object!
        self.history = history
        self.label = label # stores the command! like "add 5 3"
        # these two give the object a shared history and a calculation

    def execute(self) -> float:
        # TODO: execute the calculation, then record a successful entry.
        # Return the result. A failure must leave history unchanged.

        # execute the calculation 
        result = self.calculation.execute() # returns the result!
        # calculation is the object we created in CalcculateCommand! 
        # the calculation class has execute!, and we pull it from there

        # if calculation fails in .execute(), it will automatically never reach the line to get recorded in history

        # record the calcultion in history
        self.history.append(f"{self.label} = {result}")
        # appends the calculation to the list

        return result
 
class HistoryCommand: # cerates History objects! 
    def __init__(self, history: list[str]):
        # no need for self.calculation = calculation 
        # bc it doesnt need a calculation! just the past ones 
        self.history = history # ensures history object saves shared history! 
        # original shared list

    def execute(self): 
        return self.history.copy()
        # returns a copy of history list to be used !

    '''
 Write CalculateCommand. 
 Give it a calculation and a shared history list. 
 Its execute() must run the calculation, 
    add a successful entry to history, and return the answer. 
    If calculation fails, do not add an entry.

Write HistoryCommand with its own execute(). 
Return a copy of the history list so the caller cannot change the stored list by appending or removing entries. 
Simple strings are fine for entries. 
    For example, add 5 3 = 8.0 is readable; equivalent readable formats are accepted. 

Create the shared history list once in main(), outside the input loop.
    Give that same list to both command classes. 
    A new list on each loop would forget earlier work. 

    The CLI prints them or says that history is empty.


'''