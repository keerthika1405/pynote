text="""\t\t\t\tINTRODUCTION TO PYTHON\n\n\n
Introduction:
Python is a high-level programming language for general-purpose programming
It is an open source,interpreted, objected-oriented programming language
Python was created by a Dutch programmer, Guido van Rossum
The name of Python programming language was derived from a British sketch comedy series, Month Python's Flying Circus
The first version was released on February 20, 1991
It is a programming language which is very close to human language and because of that it is easy to learn and use.
It has been used to develop web applications, desktop applications, system adminstration, and machine learning libraries
Python is highly embraced language in the data science and machine learning community
Python is an interpreted scripting language, so it does not need to be compiled. It means it executes the code line by line\n\n
Python Syntax:
An indentation is a white space in a text
Indentation in many languages is used to increase code readability
Python uses indentation to create block of codes. In other programming languages curly brackets are used to create blocks of codes instead of indentation
One of the common bugs when writing python code is wrong indentation\n\n
Comments:
Comments are very important to make the code more readable and to leave remarks in our code
Python does not run comment parts of our code
Single Line Comment - # This is the first comment
Multiline Comment - ""This is multiline comment in python ""\n\n
Data types:
In Python there are several types of data types\n
Number
Integer: Integer(negative, zero and positive) numbers  -3, -2, -1, 0, 1, 2, 3 ...
Float: Decimal number  -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
Complex Example 1 + j, 2 + 4j\n
String
A collection of one or more characters under a single or double quote
If a string is more than one sentence then we use a triple quote
'Python'\n
Booleans
A boolean data type is either a True or False value
T and F should be always uppercase\n
List
Python list is an ordered collection which allows to store different data type items
[0, 1, 2, 3, 4, 5]  
['Banana', 'Orange', 'Mango', 'Avocado'] 
['Finland','Estonia', 'Sweden','Norway'] 
['Banana', 10, False, 9.81]\n
Dictionary
A Python dictionary object is an unordered collection of data in a key value pair format
{'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']}\n
Tuple
A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created.
They are immutable
('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya')\n
Set
A set is a collection of data types similar to list and tuple
Unlike list and tuple, set is not an ordered collection of items
set in Python stores only unique items
{2, 4, 3, 5}
{3.14, 9.81, 2.7}\n\n

Checking Data types
To check the data type of certain data/variable we use the type function
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
"""

with open("textfile.txt",'a') as f:
    f.write(text)
    f.close()