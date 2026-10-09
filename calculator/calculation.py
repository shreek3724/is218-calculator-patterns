from abc import ABC, abstractmethod
from collections.abc import Callable

# this is the factory that makes the calculations!

class Calculation(ABC): # an abstract class! 
    # runs when a calculation object is created
    def __init__(self, a: float, b: float,
                 operation: Callable[[float, float], float]):
        # each calculation object holds references to the two numbers and the required operation.
        # Each calculation owns its two numbers and chosen operation.
        self.a = a
        self.b = b
        self.operation = operation

    @classmethod
    def create(cls, a, b, operation):
        # this is the actual factory! it builds Calculation object! 

        # cls is the concrete class that called create().
        # The factory builds a new object of that class.
        return cls(a, b, operation) # so cls returns ArithmeticCalculation

    @abstractmethod
    def execute(self) -> float:  # pragma: no cover

        # every calculation must have this method! 
        # a child class will provide the behaviour of this method

        # This is the promise; concrete classes supply the real work.
        # execute() replaces get_result() and returns the answer.
        pass

class ArithmeticCalculation(Calculation):
    # child class of Calculation
    # runs the operation of the Calculation object to return a result! 
    def execute(self) -> float:
        # An instance method uses this calculation's stored values.
        return self.operation(self.a, self.b)
