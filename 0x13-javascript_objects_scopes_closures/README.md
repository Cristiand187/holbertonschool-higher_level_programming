# 0x13. Javascript - Objects, Scopes and Closures

## :books: Resources
Read or watch:
* [JavaScript object basics](https://intranet.hbtn.io/rltoken/OJ4pU6uHwfCrAclbZsk_Hg)
* [Object-oriented JavaScript](https://intranet.hbtn.io/rltoken/Uqv-UMsBUpHWQZXBf5fn0g)
* [Class - ES6](https://intranet.hbtn.io/rltoken/zMWxOmGWEsOCldCKeDswCA)
* [super - ES6](https://intranet.hbtn.io/rltoken/DTMKogwFYEgUnpLrNvTcfQ)
* [extends - ES6](https://intranet.hbtn.io/rltoken/fh2JHfNNa-HLnmfSdOo9TA)
* [Object prototypes](https://intranet.hbtn.io/rltoken/lrlwnQMM82RimJJcfLao5w)
* [Inheritance in JavaScript](https://intranet.hbtn.io/rltoken/LDpXxzBrdmmXAHoNrWwLxg)
* [Closures](https://intranet.hbtn.io/rltoken/qDa7F8060Jlhe3DZZitY4A)
* [this/self](https://intranet.hbtn.io/rltoken/ockP7FQKKmTRvfeAHw-XSw)
* [Modern JS](https://intranet.hbtn.io/rltoken/22mdHf9KeFhRQrLP-e1hPw)

---
## :bulb: Learning Objectives
What you should learn from this project:

* Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
* How to create an object in Javascript
* What this means
* What undefined means 
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another

---
## :computer: Task

### [0. Rectangle #0](./0-rectangle.js)
Write an empty class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class 


### [1. Rectangle #1](./1-rectangle.js)
Write a class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class
 * The constructor must take 2 arguments w and h
 * Initialize the instance attribute width with the value of w 
 * Initialize the instance attribute height with the value of h 


### [2. Rectangle #2](./2-rectangle.js)
Write a class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class
 * The constructor must take 2 arguments w and h
 * Initialize the instance attribute width with the value of w 
 * Initialize the instance attribute height with the value of h 
 * If w or h is equal to 0 or not a positive integer, create an empty object


### [3. Rectangle #3](./3-rectangle.js)
Write a class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class
 * The constructor must take 2 arguments: w and h
 * Initialize the instance attribute width with the value of w 
 * Initialize the instance attribute height with the value of h 
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * Create an instance method called print() that prints the rectangle using the character X


### [4. Rectangle #4](./4-rectangle.js)
Write a class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class
 * The constructor must take 2 arguments: w and h
 * Initialize the instance attribute width with the value of w 
 * Initialize the instance attribute height with the value of h 
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * Create an instance method called print() that prints the rectangle using the character X
 * Create an instance method called rotate() that exchanges the width and the height of the rectangle
 * Create an instance method called double() that multiples the width and the height of the rectangle by 2


### [5. Square #0](./5-square.js)
Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:


### [6. Square #1](./6-square.js)
Write a class Square that defines a square and inherits from Square of 5-square.js:


### [7. Occurrences](./7-occurrences.js)
Write a function that returns the number of occurrences in a list:
 * Prototype: exports.nbOccurences = function (list, searchElement)


### [8. Esrever](./8-esrever.js)
Write a function that returns the reversed version of a list:
 * Prototype: exports.esrever = function (list)
 * You are not allow to use the built-in method reverse


### [9. Log me](./9-logme.js)
Write a function that prints the number of arguments already printed and the new argument value. (see example below)
 * Prototype: exports.logMe = function (item)
 * Output format: <number arguments already printed>: <current argument value>


### [10. Number conversion](./10-converter.js)
Write a function that converts a number from base 10 to another base passed as argument:
 * Prototype: exports.converter = function (base)
 * You are not allowed to import any file
 * You are not allowed to declare any new variable (var, let, etc..)


### [11. Factor index](./100-map.js)
Write a script that imports an array and computes a new array.
 * Your script must import list from the file 100-data.js
 * You must use a map. Tips
 * A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
 * Print both the initial list and the new list


### [12. Sorted occurences](./101-sorted.js)
Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
 * Your script must import dict from the file 101-data.js
 * In the new dictionary:
	 * A key is a number of occurrences
 * A value is the list of user ids
 * Print the new dictionary at the end


### [13. Concat files](./102-concat.js)
Write a script that concats 2 files.
 * The first argument is the file path of the first source file
 * The second argument is the file path of the second source file
 * The third argument is the file path of the destination

---

## Author
* **Cristian David Pineda Vargas** - [Cristiand187](https://github.com/Cristiand187)