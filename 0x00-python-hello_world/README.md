# 0x00. Python - Hello, World

## :books: Resources
Read or watch:
* [The Python tutorial](https://intranet.hbtn.io/rltoken/fX5geNeDFcCtootbB_MqCQ)
* [Whetting Your Appetite](https://intranet.hbtn.io/rltoken/JnsZOCXrWDkZn6iMo1uuFg)
* [Using the Python Interpreter](https://intranet.hbtn.io/rltoken/AejXr_G-d8CSITEtpvwpRg)
* [An Informal Introduction to Python](https://intranet.hbtn.io/rltoken/lUBuPMNcox9EqJ1Q3oVesQ)
* [How To Use String Formatters in Python 3](https://intranet.hbtn.io/rltoken/z6mk3Yep2tJVSF6KsBAYrg)
* [Learn to Program](https://intranet.hbtn.io/rltoken/gYgGXOth8N16KjUpXgO1uQ)
* [PEP 8 – Style Guide for Python Code](https://intranet.hbtn.io/rltoken/BMIjFOY7HvWHSjHfNrkzPg)

---
## :bulb: Learning Objectives
What you should learn from this project:

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* Who created Python
* Who is Guido van Rossum
* Where does the name ‘Python’ come from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using print
* How to use strings
* What are indexing and slicing in Python
* What is the official Holberton Python coding style and how to check your code with PEP 8

---
## Task

### [0. Run Python file](./0-run)
Write a Shell script that runs a Python script.


### [1. Run inline](./1-run_inline)
Write a Shell script that runs Python code.


### [2. Hello, print](./2-print.py)
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
 * Use the function print


### [3. Print integer](./3-print_number.py)
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

* You can find the source code here
* The output of the script should be:
    - the number, followed by Battery street,
    - followed by a new line
* You are not allowed to cast the variable number into a string
* Your code must be 3 lines long
* You have to use the new print numbers tips (with .format(...))

### [4. Print float](./4-print_float.py)
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
 * You can find the source code here
 * The output of the program should be:
	 * Float:, followed by the float with only 2 digits
 * followed by a new line
 * You are not allowed to cast number to string
 * You have to use the new print formatting tips  (with .format(...))


### [5. Print string](./5-print_string.py)
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

* You can find the source code here
* The output of the program should be:
    - 3 times the value of str
    - followed by a new line
    - followed by the 9 first characters of str
    - followed by a new line
* You are not allowed to use any loops or conditional statement
* Your program should be maximum 5 lines long

### [6. Play with strings](./6-concat.py)
Complete this source code to print Welcome to Holberton School!

* You can find the source code here
* You are not allowed to use any loops or conditional statements.
* You have to use the variables str1 and str2 in your new line of code
* Your program should be exactly 5 lines long

### [7. Copy - Cut - Paste](./7-edges.py)
Complete this source code

* You can find the source code here
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 8 lines long
* word_first_3 should contain the first 3 letters of the variable word
* word_last_2 should contain the last 2 letters of the variable word
* middle_word should contain the value of the variable word without the first and last letters


### [8. Create a new sentence](./8-concat_edges.py)
Complete this source code to print object-oriented programming with Python, followed by a new line.

* You can find the source code here
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 5 lines long
* You are not allowed to create new variables
* You are not allowed to use string literals

### [9. Easter Egg](./9-easter_egg.py)
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
 * Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)


### [10. Linked list cycle](./10-check_cycle.c)
Technical interview preparation:

* You are not allowed to google anything
* Whiteboard first
* This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.

Write a function in C that checks if a singly linked list has a cycle in it.

* Prototype: int check_cycle(listint_t *list);
* Return: 0 if there is no cycle, 1 if there is a cycle

Requirements:

Only these functions are allowed: write, printf, putchar, puts, malloc, free

### [11. Hello, write](./100-write.py)
Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.
 * Use the function write from the sys module
 * You are not allowed to use print
 * Your script should print to stderr
 * Your script should exit with the status code 1
 * (Dora Korpar was a Holberton student in Cohort 0 of San Francisco)


### [12. Compile](./101-compile)
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

### [13. ByteCode -> Python #1](./102-magic_calculation.py)
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```

---

## Author
* **Cristian David Pineda Vargas** - [Cristiand187](https://github.com/Cristiand187)