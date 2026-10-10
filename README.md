# Calulator Patterns 

made a change to check if the run actions upon pushes is working


# CLI Calculator: OOP, Design Patterns, and Testing

A short assignment book for NJIT IS218. Build a terminal calculator one small step at a time. Learn static, class, and instance methods; abstraction, inheritance, polymorphism, encapsulation, and composition; Factory, Command, and Strategy; and simple SOLID responsibilities.

**Recommended: start by [forking this repository](book/00-fork-and-submit.md).** Submit the URL of your own completed repository in Canvas. Check Canvas for your deadline.

## Read the book

- [Start here: fork, build, and submit](book/00-fork-and-submit.md)
- [What your calculator must do](book/01-what-your-calculator-must-do.md)
- [Step 1: Give each part a home](book/02-step-1-give-each-part-a-home.md)
- [Step 2: Make operations with static methods](book/03-step-2-make-operations-with-static-methods.md)
- [Step 3: Make the calculation and its factory](book/04-step-3-make-the-calculation-and-its-factory.md)
- [Step 4: Select the strategy from user input](book/05-step-4-select-the-strategy-from-user-input.md)
- [Step 5: Let a command run the calculation](book/06-step-5-let-a-command-run-the-calculation.md)
- [Step 6: Connect the CLI](book/07-step-6-connect-the-cli.md)
- [Step 7: Test the behavior and reach 100% coverage](book/08-step-7-test-the-behavior-and-reach-100-coverage.md)
- [Step 8: Run tests automatically on GitHub](book/09-step-8-run-tests-automatically-on-github.md)
- [Step 9: Explain your design in STUDENT_README.md](book/10-step-9-explain-your-design-in-the-readme.md)
- [What to submit](book/11-what-to-submit.md)
- [Basic rubric — 100 points](book/12-basic-rubric-100-points.md)
- [Helpful references](book/13-helpful-references.md)

## What is included

- A working **addition** example and the calculation ABC/class factory.
- Example tests for that small starting point.
- A GitHub Actions workflow enforcing 100% line coverage.
- Chapters guiding you through the rest of the assignment.
- `STUDENT_README.md`, where you write your own explanation.

**This is a starter, not a finished calculator.** You must add subtraction, multiplication, division, commands, history, the CLI, and tests for your completed application. Passing the starter tests does not satisfy those requirements.

## Run the starter tests

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

After you implement the CLI, run `python -m calculator`. All application code belongs in `calculator/`. Keep 100% line coverage as you add code. Small, explained `# pragma: no cover` exclusions are allowed for abstract placeholders and thin startup code. Working application behavior must have tests.

Worth **100 points**. The rubric is in the book and attached to Canvas.
