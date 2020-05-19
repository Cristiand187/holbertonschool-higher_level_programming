# 0x06. Python - Classes and Objects

## :books: Resources
Read or watch:
* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/izl1kO1isRJo6h_Ce2pmhw)
* [Object-Oriented Programming](https://intranet.hbtn.io/rltoken/K5t1QFchQYs7rkt62uMo7A)
* [Properties vs. Getters and Setters](https://intranet.hbtn.io/rltoken/LZg7XYGGZj49Gu2276afpA)
* [Learn to Program 9 : Object Oriented Programming](https://intranet.hbtn.io/rltoken/aFk7Ki8TPw5vZZBx2JXvIQ)
* [Python Classes and Objects](https://intranet.hbtn.io/rltoken/CFTUXsxbTVu4xb698_2bmQ)
* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/DK1vkIQ0xT1fmMrmBcSGiA)

---
## :bulb: Learning Objectives
What you should learn from this project:

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain __dict__ of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

---
## :computer: Task

### [0. My first square](./0-square.py)
Write an empty class Square that defines a square:
 * You are not allowed to import any module


### [1. Square with size](./1-square.py)
Write a class Square that defines a square by: (based on 0-square.py)


### [2. Size validation](./2-square.py)
Write a class Square that defines a square by: (based on 1-square.py)


### [3. Area of a square](./3-square.py)
Write a class Square that defines a square by: (based on 2-square.py)


### [4. Access and update private attribute](./4-square.py)
Write a class Square that defines a square by: (based on 3-square.py)


### [5. Printing a square](./5-square.py)
Write a class Square that defines a square by: (based on 4-square.py)


### [6. Coordinates of a square](./6-square.py)
Write a class Square that defines a square by: (based on 5-square.py)


### [7. Singly linked list](./100-singly_linked_list.py)
Write a class Node that defines a node of a singly linked list by: 
 * Private instance attribute: data:
	 * property def data(self): to retrieve it
 * property setter def data(self, value): to set it:
	 * data must be an integer, otherwise raise a TypeError exception with the message data must be an integer
	 * Private instance attribute: next_node:
	 * property def next_node(self): to retrieve it
 * property setter def next_node(self, value): to set it:
	 * next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
	 * Instantiation with data and next_node: def __init__(self, data, next_node=None):


### [8. Print Square instance](./101-square.py)
Write a class Square that defines a square by: (based on 6-square.py)


### [9. Compare 2 squares](./102-square.py)
Write a class Square that defines a square by: (based on 4-square.py)


### [10. ByteCode -> Python #5](./103-magic_class.py)
Write the Python class MagicClass that does exactly the same as the following Python bytecode:

---

## Author
* **Cristian David Pineda Vargas** - [Cristiand187](https://github.com/Cristiand187)