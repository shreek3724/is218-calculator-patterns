"""These tests cover only the starter. Add tests for every feature you build."""
import pytest
from calculator.commands import CalculateCommand
from calculator.operations import Operations
from calculator.calculation import Calculation, ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand

@pytest.mark.parametrize("a,b,expected", [(5, 3, 8), (-5, 3, -2), (0, 0, 0), (1.5, 2.25, 3.75)])
def test_add(a, b, expected):
    assert Operations.add(a, b) == pytest.approx(expected)

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

def test_abstract_calculation_cannot_be_created():
    with pytest.raises(TypeError):
        Calculation.create(5, 3, Operations.add)

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