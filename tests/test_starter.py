"""These tests cover only the starter. Add tests for every feature you build."""
import pytest
from calculator.cli import main
from calculator.commands import CalculateCommand
from calculator.operations import Operations
from calculator.calculation import Calculation, ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand

@pytest.mark.parametrize("a,b,expected", [(5, 3, 8), (-5, 3, -2), (0, 0, 0), (1.5, 2.25, 3.75)])
def test_add(a, b, expected):
    assert Operations.add(a, b) == pytest.approx(expected)

# adding tests for math operations with different integer and float variations
def test_subtract():
    assert Operations.subtract(5, 3) == 2
    assert Operations.subtract(-5, 3) == -8
    assert Operations.subtract(0, 0) == 0
    assert Operations.subtract(1.5, 2.25) == -0.75

def test_multiply():
    assert Operations.multiply(5, 3) == 15
    assert Operations.multiply(-5, 3) == -15
    assert Operations.multiply(0, 0) == 0
    assert Operations.multiply(1.5, 2.25) == 3.375

def test_divide():
    assert Operations.divide(6, 3) == 2
    assert Operations.divide(-6, 3) == -2
    assert Operations.divide(0, 5) == 0
    assert Operations.divide(1.5, 2.5) == 0.6

# test to divide by zero
def test_divide_by_zero():
    with pytest.raises(ValueError):
        Operations.divide(5, 0)

# also fulfills: 
# Test factory creates concrete calculation with supplied values and operation.
def test_factory_stores_values_and_operation():
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)
    assert isinstance(calculation, Calculation)
    assert calculation.a == 5
    assert calculation.b == 3
    assert calculation.operation is Operations.add
    assert calculation.execute() == 8

def test_operation_can_be_replaced():
    calculation = ArithmeticCalculation.create(5, 3, lambda a, b: a * b)
    assert calculation.execute() == 15

# Test calculations using different operation functions.
def test_calculation_with_subtraction():
    calculation = ArithmeticCalculation.create(5, 3, Operations.subtract)
    assert calculation.execute() == 2
# checks that the Calculation obect can you dufferent math functions without changing the Calculation class!
# bc we are giving CALCULATION numbers and an operation, and it can execute the given operaion without it being hard coded in!
# you could say Operations.add, and it would still work correctly!

# also fulfills: 
# Test that Calculation class cannot be instantiated.
def test_abstract_calculation_cannot_be_created():
    with pytest.raises(TypeError):
        Calculation.create(5, 3, Operations.add)

# Test Command results
def test_command_returns_subtraction_result():
    history = [] # empty history list
    calculation = ArithmeticCalculation.create(5,3, Operations.subtract) # creates the Calculation object with two numbers and an operation
    command = CalculateCommand(calculation, history, "subtract 5, 3") # creates the actual command!
    result = command.execute() # executes the command
    assert result == 2 # checks that the result of the command is correct! 

# Test successful history entries
def test_successful_history_entries():
    history = [] # creates an empty list
    calculation = ArithmeticCalculation.create(5, 3, Operations.add) # creates the Calculation with the info
    command = CalculateCommand(calculation, history, "add 5 3") # creates the actual command!
    command.execute() # executes the command
    assert history == ["add 5 3 = 8"] # checks that the calculation has been added to the history! 

# Test no history entry after faliure
def test_failed_command_does_not_add_to_history():
    history = [] # creates an empty list
    calculation = ArithmeticCalculation.create(5, 0, Operations.divide) # creates the Calculation with the info
    command = CalculateCommand(calculation, history, "divide 5 0") # creates the actual command!

    with pytest.raises(ValueError):
        command.execute() # checks that executing the command raises a ValueError !
    
    assert history == [] # checks that no calculation has been added to the history! 
    # bc history is empty!

# Test for empty history
def test_empty_history():
    history = [] # creates an empty list
    command = HistoryCommand(history) # creates the HISTORYcommand object and gives it the empty list!
    result = command.execute() # stores the result of the command - returns a copy of history list
    assert result == [] # checks that the result is an empty list when history is empty

# check that returned history is a COPY!
def test_history_command_returns_copy():
    history = ["add 5 3 = 8"] # creates original history list
    command = HistoryCommand(history) # create the HistoryCommand object with the original history list

    result = command.execute() # executes the HistoryCommand and stores it's result in RESULT
    result.append("subtract 5 3 = 2") # modifies the returned copy in result

    assert result is not history # ensures result and history are two different list objects
    assert history == ["add 5 3 = 8"] # ensures the original history list is unchanged

# Test CLI success
def test_cli_success(monkeypatch, capsys):
    # monkeypatch - replaces keyboard input with the two commadnds "add 5 3" and "exit" (simulates keyboard input- check?)
    # capsys - captures what the cli prints

    inputs = iter(["add 5 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # lambda _ accepts the prompt argument ("> ") and ignores it.
    # next(inputs) returns the next simulated command.

    main() # main() runs the CLI as if you typed hose commands

    captured = capsys.readouterr() # captures the output from the CLI
    assert "8" in captured.out # checks that the CLI displays the correct answer

# test CLI with unknown commands
def test_cli_unknown_command(monkeypatch, capsys):
    inputs = iter(["banana", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Unknown operation" in captured.out # checks that the CLI displays an error for unknown commands

# test CLI with wrong operand counts
def test_cli_wrong_operand_count(monkeypatch, capsys):
    inputs = iter(["add 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Please enter an operation followed by two numbers" in captured.out 
    # checks that the CLI displays an error for wrong operand counts

# test CLI with invalid numbers
def test_cli_invalid_numbers(monkeypatch, capsys):
    inputs = iter(["add 5 a", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Invalid number" in captured.out # checks that the CLI displays an error for invalid numbers

# Test CLI with division by zero
def test_cli_division_by_zero(monkeypatch, capsys):
    inputs = iter(["divide 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out # checks that the CLI displays an error for division by zero

# Test CLI with continuing after errors
def test_cli_continues_after_errors(monkeypatch, capsys):
    inputs = iter(["add 5 a", "add 2 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Invalid number" in captured.out # checks that the CLI displayed the error for the first invalid input
    assert "5" in captured.out # checks that the CLI continued and displayed the output for the next valid command

# Test CLI with exit
def test_cli_exit(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == "" 
    # checks that the CLI displays an exit message
    # leave empty bc CLI does not print any message when exiting 

# Test CLI with EOF (End of File?)
# tests what happens when the input stream ends unexpectedly- like if the user presses Ctrl+D (EOF)
def test_cli_eof(monkeypatch, capsys):
    def fake_input(_):
        raise EOFError # simulates user ending input
    
    monkeypatch.setattr("builtins.input", fake_input) # replaces python's built in input() with our fake_input() function!
    main() # runs the CLI to check if it handles EOF error

    captured = capsys.readouterr() # captures the output of the CLI
    assert captured.out == "" 
    # checks that the CLI handles EOF without displaying an error message

# test added to address cli.py test coverage 
# test the empty history message
def test_cli_empty_history(monkeypatch, capsys):
    inputs = iter(["history", "exit"]) # simulates asking for history and then exiting
    monkeypatch.setattr("builtins.input", lambda _: next(inputs)) # supplies simulated commands
    main()
    captured = capsys.readouterr()
    assert "History is empty." in captured.out # checks that the CLI displays a message when history is empty

# test added to address cli.py test coverage 
# test added to address testing displaying existing history
def test_cli_displays_history(monkeypatch, capsys):
    inputs = iter(["add 5 3", "history", "exit"]) # simulates adding a command, asking for history, and then exiting
    monkeypatch.setattr("builtins.input", lambda _: next(inputs)) # supplies simulated commands
    main()
    captured = capsys.readouterr()
    assert "8" in captured.out # checks that the result of the calculation is displayed
    assert "add 5 3 = 8" in captured.out # checks that the CLI displays the existing history entry

# test added to address cli.py test coverage 
# test blank input
def test_cli_blank_input(monkeypatch, capsys):
    inputs = iter(["", "add 5 3", "exit"]) # simulates entering a blank command and then exiting
    monkeypatch.setattr("builtins.input", lambda _: next(inputs)) # supplies simulated commands
    main()
    captured = capsys.readouterr()
    assert captured.out == "8.0\n" # checks that the result of the calculation is displayed
    # we dont return anything when input is blank, so we dont need to return "Invalid Command" or anything

# test CLI then exit properly
def test_cli_exit(monkeypatch, capsys):
    answers = iter(["add 5 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    main()

    lines = capsys.readouterr().out.splitlines()
    assert any(line.strip() in ("8", "8.0") for line in lines)

# adding the CalculatorCommand test! (step 5)
#  test that checks the returned answer and the new history entry.
def test_calculate_command():
    history =[]

    # creating the calculation the test will run
    calculation = ArithmeticCalculation.create(5,3, Operations.add)
    # creating the CalculateCommand object
    command = CalculateCommand(calculation, history, "add 5 3")
    # need the same 3 pieces of info as the init for the CalculateCommand!
    # test that CalculateCOmmand returns the answer
    result = command.execute()
    # check that the output returned is correct
    assert result == 8

    # check that the history has been updated
    assert history == [f"{command.label} = {result}"]

# testing the HistoryCommand 
def test_history_command():
    history = ["add 5 3 = 8"]
    command = HistoryCommand(history)
    result = command.execute()
    assert result == [f"add 5 3 = 8"]
    assert result is not history # ensures history object is giving us a copy! 