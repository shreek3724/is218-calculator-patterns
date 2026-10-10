# My calculator submission

Actions Run Link: [Link](https://github.com/shreek3724/is218-calculator-patterns/actions/runs/38015120536)
As a plain text URL: https://github.com/shreek3724/is218-calculator-patterns/actions/runs/38015120536

## Setup, run, and test

In order to set up the project, use Python 3.12 or later, install the and project dependences with:
```bash
python -m pip install -r requirements.txt
```

Also make sure to activate the virtual environment with:
```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell instead:
# .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Then you can run the calculator with:
```bash
python -m calculator
```
And input "exit" to exit the calculator.

You can also run the tests with:
```bash
python -m pytest -v
```
And check for full coverage and run the full test suite with:
```bash
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

## Example conversation - Show arithmetic, history, an error, and exit.

Here is an example coversation of how someone may use the calculator, and the output they may see.
```bash
Enter command: add 5 3
8.0
Enter command: subtract 5 3
2.0
Enter command: history
['add 5 3 = 8.0', 'subtract 5 3 = 2.0']
Enter command: exit
```

## Static, class, and instance methods - Explain each using your own method names.

A static method is one that belongs to a class, but is not instantiated, and is essentially a global method. In the project, Operations.add() is an exaple of a static method, as it performs an operaton with supplied arguments, without needing to actually be instantiated. 

A class method is one that belongs to a class, recieves the class itself as the first argument, and is conventionally named cls. In this project, it uses cls to contruct a calculation. 

An instance method is one that recieves a specific object as its first argument, indicated by the use of "self," which is found in this project in ArithmeticCalculation.execite()- it uses values and operations stored in that calculation obejct by using self to access them. The calculation object can then execute its own calculation by accessing its own data.

## Factory, Command, and Strategy - Trace `add 5 3` through your code.

A factory pattern is one that provides a resuable method that constructs objects. In the project, it is in Calculation.create(), through ArithmeticCalculation.create(), as it creates the actual calculation object, which is then executed, When a user enters "add 5 3" the CLI supplies these values, and the Operations.add function to create an ArithmethicCalculation object.

A command pattern represents an action as an executable object, serving as a translator between input and command. This is found in the project in CalculateCommand and HistoryCommand. When tracing the input "add 5 3" the CLI creates the calculation, and passes the calculation, history list, and label to CalculateComannd. CalculateCommand.execute() then calls the calculation's execute() method, and records the successful result in history.

A strategy pattern is one that provides interchangeable algorithms to one execution logic- in this project it esentially ensures the correct operations are selected based on input. If "add 5 3" is traced in this context, CLI looks up Operations.add, which supplies that function to ArithmethicCalculation, and then the calculation invokes the supplied Operations.add function with the supplied operands, and the function returns the answer of 8.0.

## OOP - Explain encapsulation, abstraction, inheritance, polymorphism, and composition with examples from your code.

Encapsulation - This is used to keep related data and behaviour together, and to control how this data is accessed and/or changed.

In this project this is used in multple places. 

ArithmethicCalculation stores values and operations for a calculation.

CalculateCommand holds the calculation, history list, and label it needs in order to both peform and record an action.


Abstraction - This is to define what an object must do, while ensuring every implementation doesn't need to work the same way internally. It allows for flexibility, as objects can use methods without necessarily needing to know what the methods contain.

In the project, Calculation is an abstract base class that declares execute() which serves as a contract, meaning every calculation must provide it. ArithmeticCalculation can later benefit from this abtraction by provding the implementation. Operations can use execute() without needing to know how it works.


Inheritance - This describes when a child class recieves, or "inherits" behaviour from a parent class.

In the project, ArithmeticCalculation inherits from Calculation, and uses the inherited class method of create() in order to construct a calculation. This prevents from having to use the same construction logic in multiple places.


Polymorphism - This describes how different objects can all respond to the same method call, but with their own implementations.

In the project, this is expressed when a command uses calculation.execute(), as it is used on calculations depending on their specific implementation. The different calculations classes all provide their own execite() behaviour while still following the same contract.


Composition - This refers to building an object by combining other objects or components it uses.

In the project this is shown in CalculateCommand, when it holds a calculation it executes, while ArithmethicCalculation holds the operation function that performs the math. This seperates the command-running aspect from the actual resultc-calculation aspect.

## SOLID - Give one short example for each principle. Describe adding another operation without changing calculation execution.

Single Responsibility Principle - It means each component has one job. In this project, Operations handles the math/arithmetic, Calculations defiines the calculation contract, HistoryCommand retrives history, and more. 


Open/Closed Principle - It means to extend functionality without having to rewrite existing code that handles general behaviour. In this project, it can be seen where the operations dictionary maps operation names to functions.

Liskov Subsitution Principle - It means that a replacement for a base class should maintain and honor the same contract, to ensure existing code can use it correctly. This also helps reduce redunancies. In the project it can be found when a command that recieves a Calculation object expects it to have execute(), in order to return a result or raise an error accordingly.

Interface Segregation Principle - It means a class should not be forced to implement any methods that are unrelated or unecessary. In the project it can be seem where Calculation uses execute() as its core interface, and does not do anything else, like managing history, for example.

Dependency Inversion Principel - This means that structure should depend on a general contract, or supplied behaviour, rather than having a hard-coded and specific impplementation. This allows for flexibility. An example of this in the project is when CalculateCommand recieves a calculation, rather than internally contructing arithmetic,or in ArithmeticCalculation, where it recieves an operation function, rather than hard coding it within itself.

## Tests and GitHub Actions

Actions Run Link: [Link](https://github.com/shreek3724/is218-calculator-patterns/actions/runs/38015120536)
As a plain text URL: https://github.com/shreek3724/is218-calculator-patterns/actions/runs/38015120536
These confirm 100% line coverage.

## Coverage exclusions

The starter excludes the abstract `Calculation.execute()` placeholder because it declares the contract and supplies no implementation. List and explain any other exclusions you add.

calculator/__main__.py : The if __name__ == "__main__": entry point is excluded from coverage. This is because it only launches main if the CLI behaviour is directly tested.

This approach should work, but I was running into problems with it, so I created a .coverage arc file, and included these lines:
[run]
omit = calculator/__main__.py
