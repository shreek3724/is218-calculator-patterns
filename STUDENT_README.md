# My calculator submission

Replace these prompts with your own short explanations.

## Setup, run, and test

Write the commands for your completed project.

## Example conversation

Show arithmetic, history, an error, and exit.

## Static, class, and instance methods

Explain each using your own method names.

## Factory, Command, and Strategy

Trace `add 5 3` through your code.

## OOP

Explain encapsulation, abstraction, inheritance, polymorphism, and composition with examples from your code.

## SOLID

Give one short example for each principle. Describe adding another operation without changing calculation execution.

## Tests and GitHub Actions

Add your successful Actions run URL and confirm 100% line coverage.

## Coverage exclusions

The starter excludes the abstract `Calculation.execute()` placeholder because it declares the contract and supplies no implementation. List and explain any other exclusions you add.

calculator/__main__.py : The if __name__ == "__main__": entry point is excluded from coverage. This is because it only launches main if the CLI behaviour is directly tested.
This should work, but I was running into problems, so I created a .coverage arc file, and included these lines:
[run]
omit = calculator/__main__.py
