#!/usr/bin/env python3
def fizzbuzz():

    num = 1
    
    while (num <= 100):
        str = ""
        if (num % 5 is 0 and num % 3 is 0):
            str = "FizzBuzz"
        elif (num % 5 is 0):
            str = "Buzz"
        elif (num % 3 is 0):
            str = "Fizz"
        if (str == ""):
            print(num, end=" ")
        else:
            print(str, end=" ")
        num = num + 1
