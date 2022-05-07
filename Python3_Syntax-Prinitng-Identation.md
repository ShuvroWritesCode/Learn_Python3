# Python Syntax
Python is an interpreter based simple syntax language. It was created by Guido van Rossum, and released in 1991. It is used in multi-platform and it has many used cases like machine learning, backend web development, automation etc.

A python program requires less amount of syntax than most other languages. Here is a python program printing Hello, World!

      print("Hello, World!")

#Printing in Python

Unlike other languages, one can use different ways to print sentence in python.
First way is to use single quotations ' '

    print('Hello, World!')

Second way is using double quotations " "

    print("Hello, World!")

Double quotation technique is useful while you are trying to print a sentence which already holds an apostrophe in it.
For example,

    print("Welcome to McDonald's!")

Another way is very different and it makes python very unique. The way is to write using three single quotations ' ' 'sentence here' ' '

        print('''Python for beginners!''')

The final way is to write using format string method. The syntax goes like,

    number = 93
    name = 'John'
    print(f"Congratulations! {name} got {number} in his last test!")

Output: 
> Congratulations! John got 93 in his last test!

#Python Indentation

Indentation is basically spacing before a line 

Identation plays a very important role in python language. In other language like C, indentation is used for readablity but in python, your code might not be executed if your identation is incorrect.

The number of space for indentation is upto the coder, but using 4 spaces is good practice. But in a code block, the number of spaces for an indentation should be equal.

    if 99 < 100:
    			print("Ninety nine is less than one hundred")
