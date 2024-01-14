# 0x00. AirBnB clone - The console

## Description

This project is a Python package that includes a command interpreter built using the `cmd` module. The interpreter provides a user-friendly interface to execute various commands and perform specific actions. Additionally, the project incorporates unit testing, serialization/deserialization of classes, handling datetime, UUID, *args, **kwargs, and named arguments in functions.

## Command Interpreter:

The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter  serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:
- show
- create
- update
- destroy
- count

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Doing operations on objects (count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object

### How to start

To start the command interpreter, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Run the interpreter script using the command: `./interpreter.py`

### How to use

Once the interpreter is running, you can enter commands and interact with the functionalities. Use the `help` command to get information about available commands and their usage.

### Examples

Here are some examples of commands:

```bash
$ ./interpreter.py
>>> command1 arg1 arg2
Output of command1 with arguments arg1 and arg2
>>> command2
Output of command2
