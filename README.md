 AirBnB clone - The console Project

This project is a simple command-line interpreter for the HBNB project as part of a pair programming effort for the ALX Software Engineering program. It provides a basic interactive shell where users can execute commands related to managing objects in a HBNB application.

#Project Requirements.

## Command Interpreter
The command interpreter is implemented using the `cmd` module in Python. It supports commands such as `quit` to exit the program, `EOF` to exit using Ctrl+D, and provides acustom prompt `(hbnb)` for user interaction. The interpreter ignores empty lines, and the `help` command is available to display information about supported commands.

#Usage

The hbnb can be used in interactive mode or non-interactive mode as follows.

#Interactive Mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

#Non-Interactive Mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

#Here are some examples of using the HBNB Command Interpreter:

Exiting the interpreter:

    (hbnb) quit

Using EOF to exit:

    (hbnb) <Ctrl+D>

Getting help:

    (hbnb) help

Other commands:

    (hbnb) <your-command-here>

#Authors

This project was developed by Tanatswa Gendere and Tatenda Torerwa for the ALX Software Engineering Program Program. See AUTHORS.
