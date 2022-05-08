## Variable in Python
Varables are containers to store any value. The value can be any integer, decimal, complex number or even any string. In python, when we assign a value, a variable is created. Here, declaration of variable is not possible. Unlike C or C++, here we do not need to mention the data type. Python consider data type for each variable by itself just looking at the assigned value to it.

    x = 5
    y = 3.2
    c = 'Bangladesh'
    list = [1, 2, 3, 4, 0]

Variables are always Case-sensitive. 

    a = 5.12
    A = 3.1416
    # a and A variables are different. A will not override a here.

### Variable naming rule
Variable names can be both short or something that holds meaning. But giving a descriptive name that holds meaning is preferable for readability. 
The variable name can never start with any digit. It can never have any spaces or hyphen '-' in between. 
It should only hold apha-numeric characters (0-9, A-Z, a-z) and spaced with underscores. 

Illegal naming:
    
    2x = 5
    my-var = 3.22
    7his-1s-v4r(1) = 'illegal'

Legal naming:
    
    x = "5"
    Y = True
    var1 = 3.4367
    _var1 = 'Bangladesh'
    secret_num = 9
    LIST_2 = [0, 1, 2, 3, 10, 64, 82]

### Multi Words Variable Names
Descriptive names as variable with more than one word can be difficult to read. There are several techniques to make them more readable.
#### Pascal Case
Each word starts with a capital letter:

    FirstSecretNumber = 9
#### Camel Case
Each word, except the first, starts with a capital letter:

    firstSecretNumber = 9
#### Snake Case
Each word is separated by an underscore character:

	first_secret_number = 9

### One Value to Multiple Variables
To assign same value in multiple variable we use an equal sign in between them.

	x = y = z = 10
	print(x)
	print(y)
	print(z)
  
Output:
>10
>
>10
>
>10

### Variables Output
print() function is used to print varables. There are multiple technique printing variables. Coder needs to use these ways based on their necessity. 

	x = "Learn Python3"
	print(x)

Output: 
> Learn Python3

One can print a string by assigning each word to single variable and printing the variables by comma , in between them.

	x = 'Python'
	y = 'for'
	z = 'beginner'
	print(x, y, z)

Output:
> Python for beginner

Same thing can be done by placing plus symbol + in between. But in this case, the spaces between words are removed.

	x = 'Python'
	y = 'for'
	z = 'beginner'
	print(x + y + z)

Output:
> Pythonforbeginner

To solve this problem we need to add a space character after each word while assigning the variable.
	x = 'Python '
	y = 'for '
	z = 'beginner '
	print(x + y + z)

Output:
> Python for beginner

If variables hold numbers, then + character works as a mathematical operator.

	x = 10
	y = 5
	print(x + y)

Output:
> 15

In the print() function, you cannot print two different data type variables together with + character. Terminal will show an error for it.

	x = 5
	y = "John"
	print(x + y)

Output:
> TypeError: unsupported operand type(s) for +: 'int' and 'str'
