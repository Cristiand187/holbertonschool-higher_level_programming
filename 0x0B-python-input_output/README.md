# 0x0B. Python - Input/Output

## :books: Resources
Read or watch:
* [7.2. Reading and Writing Files](https://intranet.hbtn.io/rltoken/c5ypFfQwcM-SZ-7tr3WuxA)
* [8.7. Predefined Clean-up Actions](https://intranet.hbtn.io/rltoken/1wqMFejKqBva-Lxws0lftw)
* [Dive Into Python 3: Chapter 11. Files](https://intranet.hbtn.io/rltoken/8aSPOpBZj9B1DB6GfoEWfg)
* [JSON encoder and decoder](https://intranet.hbtn.io/rltoken/XBqM3BrA_rUBw6DXw4X98Q)
* [Learn to Program 8 : Reading / Writing Files](https://intranet.hbtn.io/rltoken/derf9VLFVDnSgX2n-drwnw)
* [Automate the Boring Stuff with Python](https://intranet.hbtn.io/rltoken/Y77h8aeRoljlN643yKfdTg)

---
## :bulb: Learning Objectives
What you should learn from this project:

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* How to open a file
* How to write text in a file
* How to read the full content of a file 
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the with statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string 
* How to convert a JSON string to a Python data structure

---
## :computer: Task

### [0. Read file](./0-read_file.py)
Write a function that reads a text file (UTF8) and prints it to stdout:
 * Prototype: def read_file(filename=""):
 * You must use the with statement
 * You don’t need to manage file permission or file doesn't exist exceptions.
 * You are not allowed to import any module


### [1. Number of lines](./1-number_of_lines.py)
Write a function that returns the number of lines of a text file:
 * Prototype: def number_of_lines(filename=""):
 * You must use the with statement
 * You don’t need to manage file permission or file doesn't exist exceptions.
 * You are not allowed to import any module


### [2. Read n lines](./2-read_lines.py)
Write a function that reads n lines of a text file (UTF8) and prints it to stdout:


### [3. Write to a file](./3-write_file.py)
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
 * Prototype: def write_file(filename="", text=""):
 * You must use the with statement
 * You don’t need to manage file permission exceptions.
 * Your function should create the file if doesn’t exist.
 * Your function should overwrite the content of the file if it already exists.
 * You are not allowed to import any module


### [4. Append to a file](./4-append_write.py)
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
 * Prototype: def append_write(filename="", text=""):
 * If the file doesn’t exist, it should be created
 * You must use the with statement
 * You don’t need to manage file permission or file doesn't exist exceptions.
 * You are not allowed to import any module


### [5. To JSON string](./5-to_json_string.py)
Write a function that returns the JSON representation of an object (string):
 * Prototype: def to_json_string(my_obj):
 * You don’t need to manage exceptions if the object can’t be serialized.


### [6. From JSON string to Object](./6-from_json_string.py)
Write a function that returns an object (Python data structure) represented by a JSON string:
 * Prototype: def from_json_string(my_str):
 * You don’t need to manage exceptions if the JSON string doesn’t represent an object.


### [7. Save Object to a file](./7-save_to_json_file.py)
Write a function that writes an Object to a text file, using a JSON representation:
 * Prototype: def save_to_json_file(my_obj, filename):
 * You must use the with statement
 * You don’t need to manage exceptions if the object can’t be serialized.
 * You don’t need to manage file permission exceptions.


### [8. Create object from a JSON file](./8-load_from_json_file.py)
Write a function that creates an Object from a “JSON file”:
 * Prototype: def load_from_json_file(filename):
 * You must use the with statement
 * You don’t need to manage exceptions if the JSON string doesn’t represent an object.
 * You don’t need to manage file permissions / exceptions.


### [9. Load, add, save](./9-add_item.py)
Write a script that adds all arguments to a Python list, and then save them to a file:
 * You must use your function save_to_json_file from 7-save_to_json_file.py
 * You must use your function load_from_json_file from 8-load_from_json_file.py
 * The list must be saved as a JSON representation in a file named add_item.json
 * If the file doesn’t exist, it should be created
 * You don’t need to manage file permissions / exceptions.


### [10. Class to JSON](./10-class_to_json.py)
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
 * Prototype: def class_to_json(obj):
 * obj is an instance of a Class
 * All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
 * You are not allowed to import any module


### [11. Student to JSON](./11-student.py)
Write a class Student that defines a student by:
 * Public instance attributes: 
	 * first_name
 * last_name
 * age
 * Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
 * Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py)
 * You are not allowed to import any module


### [12. Student to JSON with filter](./12-student.py)
Write a class Student that defines a student by: (based on 11-student.py)


### [13. Student to disk and reload](./13-student.py)
Write a class Student that defines a student by: (based on 12-student.py)


### [14. Pascal's Triangle](./14-pascal_triangle.py)
Technical interview preparation: 


### [15. Search and update](./100-append_after.py)
Write a function that inserts a line of text to a file, after each line containing a specific string (see example):
 * Prototype: def append_after(filename="", search_string="", new_string=""):
 * You must use the with statement
 * You don’t need to manage file permission or file doesn't exist exceptions.
 * You are not allowed to import any module


### [16. Log parsing](./101-stats.py)
Write a script that reads stdin line by line and computes metrics:
 * Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
 * Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
	 * Total file size: File size: <total size>
 * where  is the sum of all previous  (see input format above)
 * Number of lines by status code: 
	 * possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
 * if a status code doesn’t appear, don’t print anything for this status code
 * format: <status code>: <number>
 * status codes should be printed in ascending order



### [17. Hack the VM](./read_write_heap.py)
Write a script that finds a string in the heap of a running process, and replaces it.
 * Read The /proc filesystem
 * Usage: read_write_heap.py pid search_string replace_string
 * where pid is the pid of the running process
 * and strings are ASCII
 * The script should look only in the heap of the process
 * Output: you can print whatever you think is interesting
 * On usage error, print an error message on stdout and exit with status code 1

---

## Author
* **Cristian David Pineda Vargas** - [Cristiand187](https://github.com/Cristiand187)