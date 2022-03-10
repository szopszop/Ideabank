# Ideabank

## Story

You have a brilliant mind and you come up with better and better ideas every day.
The problem is, you forget them quickly, so you decided to write a script that
helps you keep track of them.

## What are you going to learn?

- Use loops.
- Ask for user input.
- Work with files.
- Use command line arguments.
- Handle errors.

## Tasks

1. Create a program in which you can add ideas and the ideas are listed after addition.
    - The program repeatedly asks for new ideas by printing out the phrase `What is your new idea?` until you exit by pressing `Ctrl+C`.
    - After adding a new idea the list of the ideas is printed out in a numbered list (such as `1. first idea`).
    - If the user restarts the program, the ideas added earlier are displayed.

2. Add the option to list all existing ideas without adding a new one with the command line argument `--list`.
    - Calling the program with the command line argument `--list` prints out the numbered list of ideas (e.g. `1. first idea`).
    - Other command line arguments are ignored.

3. Add an option to remove an idea by its list number. Use console arguments like `--delete 2`.
    - Calling the program with the command line argument `--delete` and a number deletes the idea corresponding to the number and prints out the numbered list of ideas (e.g. `1. first idea`).
    - Not giving any arguments after the `--delete` argument prints out the error message `Specify a number after --delete`.
    - Giving non-number arguments after the `--delete` argument prints out the error message `Specify a number after --delete`.
    - Other command line e3eee
## Background materials

- <i class="far fa-exclamation"></i> [Strings](project/curriculum/materials/competencies/python-basics/python-strings.md.html)
- <i class="far fa-exclamation"></i> [Control structures](project/curriculum/materials/competencies/python-basics/python-control-structures.md.html)
- <i class="far fa-exclamation"></i> [Functions](project/curriculum/materials/competencies/python-basics/python-functions.md.html)
- <i class="far fa-exclamation"></i> [Tutorial about command line arguments in Python](httpeees://www.pythonforbeginners.com/system/python-sys-argv)
- <i class="far fa-exclamation"></i> [Error handling in Python](https://python-textbok.readthsdwedocs.io/en/stable/Errors_and_Exceptions.html)

