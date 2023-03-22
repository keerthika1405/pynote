text=""" \t\t\t BUILD-IN-FUNCTION\n\n\n
In Python we have lots of built-in functions
Built-in functions are globally available foryour use ,that mean you can make use of the built-in functions 
without importing or configuring
	
Built-in Functions:
abs()
all()
any()
ascii()
bin()
bool()
breakpoint()
bytearray()
bytes()
callable()
chr()
classmethod()
compile()
complex()
delattr()
dict()
dir()
divmod()
enumerate()
eval()
exec()
filter()
float()
format()
frozenset()
getattr()
globals()
hash()
help()
hex()
hasattr()
id()
input()
int()
isinstance()
issubclass()
iter()
len()
list()
locals()
memoryview()
min()
map()
max()
next()
object()
oct()
open()
ord()
pow()
print()
property()
range()
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()
__import__()\n\n\n


1.abs(x)
Return the absolute value of a number 
The argument may be an integer, a floating point number, or an object implementing __abs__()
If the argument is a complex number, its magnitude is returned 
eg: abs(-5)=5
    abs(-1j) == abs(1j) -->True
    abs(-3j * 5 + 4) -->15.524174696260024\n

2.all(iterable)
Return True if all elements of the iterable are true (or if the iterable is empty)
iterable--An iterable object (list, tuple, dictionary)

eg:  mylist = [0, 1, 1]
     x = all(mylist) -->False

     mytuple = (0, True, False)
     x = all(mytuple) --False

    mydict = {0 : "Apple", 1 : "Orange"}
    x = all(mydict) -->False

    def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True \n

3.any(iterable)
Return True if any element of the iterable is true and If the iterable is empty, return False
iterable--An iterable object (list, tuple, dictionary)

eg: def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

    mylist = [False, True, False]
    x = any(mylist)

4.ascii(object)
The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc)
The ascii() function will replace any non-ascii characters with escape characters
The ASCII value of the lowercase alphabet is from (97 to 122) And
the ASCII value of the uppercase alphabet is from (65 to 90)
(American Standard Code for Information Interchange)

eg : x = ascii("My name is Ståle")--> å will be replaced with \xe5\n

5.bin(x)
The bin() function returns the binary version of a specified integer
The result will always start with the prefix 0b
x--	Required, An integer
If x is not a Python int object, it has to define an __index__() method that returns an integer
If prefix “0b” is desired or not, you can use either of the following ways

eg:format(14, '#b'), format(14, 'b') -->  ('0b1110', '1110')
   f'{14:#b}', f'{14:b}' -->  ('0b1110', '1110')

eg :bin(3) -->'0b11'
    bin(-10)--> '-0b1010'\n

6.bool()
The bool() function returns the boolean value of a specified object
ie:one of True or False
The object will always return True, unless:
                                          The object is empty, like [], (), {}
                                          The object is False
                                          The object is 0
                                          The object is None
bool(object)--object Any object, like String, List, Number etc\n

7.breakpoint(*args)
The Python breakpoint() built-in function is a tool that allows developers to set points in code at which a debugger is called. By default, 
this function results in an instantiation of Pythons native debugger class
Since 3.7 however, developers can easily override this behavior and use the Python breakpoint() function to execute custom actions
breakpoint() will automatically call that, allowing you to drop into the debugger of choice

eg: for i in range(5):
        print(i)
    if i == 3:
       breakpoint() --># Output
                                0
                                1
                                2
                                3
                                # Create a loop over 5 integers
c:\\users\\user\\path\\to\\your\\project\\example.py(24)<module>()
-> for i in range(5):
(Pdb) 

8.bytearray()
It has a built-in data type called byte arrays, which are useful for handling
binary data such as images, audio files, and network packets
eg:
import time
# Using byte array
start = time.time()
my_bytes = bytearray(range(1000000))
my_bytes[500000] = 255
end = time.time()
print("Time taken with byte array: ", end-start)

# Using list of integers
start = time.time()
my_list = list(range(1000000))
my_list[500000] = 255
end = time.time()
print("Time taken with list of integers: ", end-start)-->  Time taken with byte array: 0.00032591819763183594
                                                           Time taken with list of integers: 0.016950130462646484
As we can see, manipulating a byte array is almost 50 times faster than manipulating a list of integers 

9.callable(object)
The callable() method takes only one argument, an object and returns one of the two values:
returns True, if the object appears to be callable.
returns False, if the object is not callable.
object	The object you want to test if it is callable or not.
classes are callable (calling a class returns a new instance)
instances are callable if their class has a __call__() method

eg: def x():
       a = 5
    print(callable(x)) -->True
    x = 5
    print(callable(x)) -->False

10.chr()
Get the character that represents the unicode 97:
chr(number)-- number An integer representing a valid Unicode code point
Convert back to unicode with the ord() function
eg: x = chr(97) -->a
    
    
11.classmethod()The classmethod() is an inbuilt function in Python,
which returns a class method for a given function
fun: the function that needs to be converted into a class method
returns: a class method for 
class C:
    @classmethod
    def f(cls, arg1, arg2): 
A class method can be called either on the class (such as C.f()) 
or on an instance (such as C().f())

eg:
    class geeks:
        course = 'DSA'
 
    def purchase(obj):
        print("Purchase course : ", obj.course)
    geeks.purchase = classmethod(geeks.purchase)
    geeks.purchase()  -->Purchase course :  DSA

12.compile()
If the (Python code) is in string form or is an AST object,
and you want to change it to a (code object), then you can use compile() method.
The code object returned by the compile() method can later be called using methods like: exec() and eval() 

compile(source, filename, mode, flag, dont_inherit, optimize) -- source-The source to compile, can be a String, a Bytes object, or an AST object
                                                              --filename-The name of the file that the source comes from.
                                                              --mode	Required. Legal values:
                                                                        eval - if the source is a single expression
                                                                        exec - if the source is a block of statements
                                                                        single - if the source is a single interactive statement
                                                              --flags  	Optional. How to compile the source. Default 0
                                                              --dont-inherit	Optional. How to compile the source. Default False
                                                              --optimize	Optional. Defines the optimization level of the compiler. Default -1                   
eg: x = 50
    # Note eval is used for statement
    a = compile('x == 50', '', 'eval')
    print(eval(a)) -->True

   x = 50
   # Note eval is used for single statement
   a = compile('x', 'test', 'single')
   print(type(a))
   exec(a) --> <class 'code'> 50

13.complex()
Return a complex number with the value real + imag*1j or convert a string or number to a complex number
complex(real, imaginary)
real-Required,A number representing the real part of the complex number,Default 0
imaginary	Optional. A number representing the imaginary part of the complex number ,Default 0
The real number can also be a String, like this '3+5j', when this is the case, the second parameter should be omitted
 
eg: x = complex('3+5j')
    print(x)   -->(3+5j)
    x = complex(3, 5)
    print(x)   -->(3+5j)

14.delattr()
The delattr() function will delete the specified attribute from the specified object
delattr(object, attribute) --object	Required. An object.
                             attribute	Required. The name of the attribute you want to remove
The getattr() function, to get the value of an attribute
The hasattr() function, to check if an attribute exist
The setattr() function, to set the value of an attribute

15.dict()
Create a dictionary containing personal information
eg: x = dict(name = "John", age = 36, country = "Norway")
    print(x)--> {'name': 'John', 'age': 36, 'country': 'Norway'}

16.dir()
--diectory
The dir python function is responsible for returning all the valid list of attributes of the object
eg:  lang = ("C","C++","Java","Python")  
     # Calling function  
     att = dir(lang)  
     # Displaying result  
     print(att)  --> ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
                     '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
                     '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
                     '__subclasshook__', 'count', 'index']

    class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']
    s = Shape()
    dir(s)--> ['area', 'location', 'perimeter']   

17.divmod(a, b)         
Display the quotient and the remainder of 5 divided by 2
The divmod() function returns a tuple containing the quotient  and the remainder when argument1
(dividend) is divided by argument2 (divisor)
divmod(dividend, divisor)
dividend	A Number. The number you want to divide
divisor	A Number. The number you want to divide with

eg: x = divmod(5, 2)
    print(x) --> (2, 1)


18.enumerate()
Convert a tuple into an enumerate object
enumerate() returns a tuple containing a count (from start which defaults to 0)
and the values obtained from iterating over iterable.
eg: x = ('apple', 'banana', 'cherry')
    y = enumerate(x)
    print(list(y))-->[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

19.eval() 
Evaluate the expression 'print(55)'
eval(expression, globals, locals)
                                expression	A String, that will be evaluated as Python code
                                globals	Optional. A dictionary containing global parameters
                                locals	Optional. A dictionary containing local parameters
eg: x = 'print(55)'
    eval(x)--> 55
    x = 1
    eval('x+1')-->2

20.exec()
Execute a block of code
exec(object, globals, locals)
                            object	A String, or a code object
                            globals	Optional. A dictionary containing global parameters
                            locals	Optional. A dictionary containing local parameters
eg: x = 'name = "John"\nprint(name)'
    exec(x)-->John


21.filter()
Construct an iterator from those elements of iterable for which function returns true , If function is None, the identity function is assumed, that is,
all elements of iterable that are false are removed
(The filter() function returns an iterator were the items are
filtered through a function to test if the item is accepted or not)
filter(function, iterable)
                        --function	A Function to be run for each item in the iterable
                        --iterable	The iterable to be filtered
Filter the array, and return a new array with only the values equal to or above 18
eg: ages = [5, 12, 17, 18, 24, 32]
    def myFunc(x):
        if x < 18:
            return False
        else:
            return True
    adults = filter(myFunc, ages)
    for x in adults:
    print(x) -->18 24 32

22.float()
Convert the number 3 into a floating point number
eg: x = float(3)
    print(x) -->3.0
    x = float("3.500")
    print(x) -->3.5
    float('-Infinity') --> -inf
    float('+1.23') --> 1.23
    float('   -12345\n')--> -12345.0
    float('1e-003')--> 0.001
    float('+1E6')--> 1000000.0

23.format()
The format() function formats a specified value into a specified format
format(value, format)
                    value	A value of any format
                    format	The format you want to format the value into.
                            Legal values:
                            '<' - Left aligns the result (within the available space)
                            '>' - Right aligns the result (within the available space)
                            '^' - Center aligns the result (within the available space)
                            '=' - Places the sign to the left most position
                            '+' - Use a plus sign to indicate if the result is positive or negative
                            '-' - Use a minus sign for negative values only
                            ' ' - Use a leading space for positive numbers
                            ',' - Use a comma as a thousand separator
                            '_' - Use a underscore as a thousand separator
                            'b' - Binary format
                            'c' - Converts the value into the corresponding unicode character
                            'd' - Decimal format
                            'e' - Scientific format, with a lower case e
                            'E' - Scientific format, with an upper case E
                            'f' - Fix point number format
                            'F' - Fix point number format, upper case
                            'g' - General format
                            'G' - General format (using a upper case E for scientific notations)
                            'o' - Octal format
                            'x' - Hex format, lower case
                            'X' - Hex format, upper case
                            'n' - Number format
                            '%' - Percentage format

24.frozenset() 
The frozenset() function returns an unchangeable frozenset object
(which is like a set object, only unchangeable)
frozenset(iterable)--iterable	An iterable object, like list, set, tuple
Try to change the value of a frozenset item.
This will cause an error:
eg: mylist = ['apple', 'banana', 'cherry']
    x = frozenset(mylist)
    x[1] = "strawberry"-->Traceback (most recent call last):
                          File "./prog.py", line 3, in <module>
                          TypeError: 'frozenset' object does not support item assignment

25.getattr()
Get the value of the "age" property of the "Person" object
getattr(object, attribute, default)
                           object	Required. An object.
                           attribute	The name of the attribute you want to get the value from
                           default	Optional. The value to return if the attribute does not exist
eg: class Person:
    name = "John"
    age = 36
    country = "Norway"   
    x = getattr(Person, 'age')
    print(x)-->36

26.globals()
The globals() function returns the global symbol table as a dictionary
A symbol table contains necessary information about the current program
globals()
eg: x = globals()
    print(x)--> {'__name__': '__main__', '__doc__': None, '__package__': None,
                 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x02A8C2D0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
                 '__file__': 'demo_ref_globals.py', '__cached__': None, 'x'_ {...}}
    x = globals()
    print(x["__file__"])- ->demo_ref_globals2.py--Get the filename of the current program

    
27.hasattr()
The hasattr() function returns True if the specified object has the specified attribute, otherwise False
hasattr(object, attribute)
                     object	Required, An object
                     attribute	The name of the attribute you want to check if exists
Check if the "Person" object has the "age" property
eg:class Person:
   name = "John"
   age = 36
   country = "Norway"
   x = hasattr(Person, 'age')
   print(x)-->True

28.hash()
Returns the hash value of a specified object
Hash values are integers
A Hash Value is a numeric value resulting from a mathematical algorithm applied to a set of data such as a file
A common hash value is called the MD5 Hash of a computer file
Every computer file in existence has a unique MD5 Hash
Hash Values can be thought of as fingerprints for files. The contents of a file are processed through a cryptographic algorithm
and a unique Hash Value is generated that identifies the contents of the file

29.help()
Invoke  the built-in help system
If no argument is given, the interactive help system starts on the interpreter console
If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic,
and a help page is printed on the console

30.hex()
Convert an integer number to a lowercase hexadecimal string prefixed with “0x
eg: x = hex(255)
    print(x)--> 0xff
    '%#x' % 255, '%x' % 255, '%X' % 255-->('0xff', 'ff', 'FF')
    format(255, '#x'), format(255, 'x'), format(255, 'X')-->('0xff', 'ff', 'FF')
    f'{255:#x}', f'{255:x}', f'{255:X}'-->('0xff', 'ff', 'FF')

31.id()
Return the unique id of a tuple object
All objects in Python has its own unique id
The id is assigned to the object when it is created (except for some object that has a constant unique id, like integers from -5 to 256)
id(object)
         object	-Any object, String, Number, List, Class 
eg: x = ('apple', 'banana', 'cherry')
    y = id(x)
    print(y)--> # This value is the memory address of the object and will be different every time you run the program

32.input()
Ask for the user's name and print it
eg: print('Enter your name:')
    x = input()
    print('Hello, ' + x)

    x = input('Enter your name:')
    print('Hello, ' + x)

33.int()
The int() function converts the specified value into an integer number
int(value, base)
                value	A number or a string that can be converted into an integer number
                base	A number representing the number format. Default value: 10
Convert the number 3.5 into an integer
eg: x = int(3.5)-->3
    x = int("12")
    print(x)-->12

34.isinstance
The isinstance() function returns True if the specified object is of the specified type, otherwise False.
isinstance(object, type)
                        object	Required. An object.
                        type	A type or a class, or a tuple of types and/or classes

Check if the number 5 is an integer:
eg: x = isinstance(5, int)-->True
    class myObj:
    name = "John"
    y = myObj()
    x = isinstance(y, myObj)
    print(x)--> True

35.issubclass()
This functionis to check if an object is a subclass of another object
returns True if the specified object is a subclass of the specified object, otherwise False.
issubclass(object, subclass)
                           object	Required. An object.
                           subclass	A class object, or a tuple of class objects 
Check if the class myObj is a subclass of myAge:
eg: class myAge:
    age = 36
    class myObj(myAge):
    name = "John"
    age = myAge
    x = issubclass(myObj, myAge)-->True

36.iter()
The iter() function returns an iterator object
iter(object, sentinel)
                    object	Required. An iterable object
                    sentinel	Optional. If the object is a callable object the iteration will stop when the returned value is the same as the sentinel
eg: x = iter(["apple", "banana", "cherry"])
    print(next(x))
    print(next(x))
    print(next(x))-->apple banana cherry

37.len()
The len() function returns the number of items in an object
When the object is a string, the len() function returns the number of characters in the string
len(object)
        object	Required. An object. Must be a sequence or a collection
eg: mylist = "Hello"
    x = len(mylist)
    print(x)-->5

38.list()
The list() function creates a list object
A list object is a collection which is ordered and changeable
list(iterable)
            iterable	Optional. A sequence, collection or an iterator object
eg: x = list(('apple', 'banana', 'cherry'))
    print(x)-->['apple', banana', 'cherry']

39.locals()
The locals() function returns the local symbol table as a dictionary
A symbol table contains necessary information about the current program
eg: x = locals()
    print(x["__file__"])-->demo_ref_globals2.py
    x = locals()
    print(x)-->{'__name__': '__main__', '__doc__': None, '__package__': None, 
                '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0327C2D0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'demo_ref_globals.py',
                '__cached__': None, 'x'_ {...}}

40.map()
The map() function executes a specified function for each item in an iterable
The item is sent to the function as a parameter
map(function, iterables)
                        function	Required. The function to execute for each item
                        iterable	Required. A sequence, collection or an iterator object. You can send as many iterables as you like, 
                                    just make sure the function has one parameter for each iterable.
eg: def myfunc(a):
    return len(a)
    x = map(myfunc, ('apple', 'banana', 'cherry'))
    print(x)
    #convert the map into a list, for readability
    print(list(x))--> <map object at 0x056D44F0> [5, 6, 6]

    def myfunc(a, b):
    return a + b
    x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
    print(x)
    #convert the map into a list, for readability:
    print(list(x))--> <map object at 0x034244F0> ['appleorange', 'bananalemon', 'cherrypineapple']

41.max()
The max() function returns the item with the highest value, or the item with the highest value in an iterable
max(n1, n2, n3, ...)--n1, n2, n3, ...	One or more items to compare
max(iterable)--iterable	An iterable, with one or more items to compare
eg: x = max("Mike", "John", "Vicky")
    print(x)--> vicky #Return the name with the highest value, ordered alphabetically
    a = (1, 5, 3, 9)
    x = max(a)
    print(x)--> 9 #Return the item in a tuple with the highest value:

42.memoryview()
The memoryview() function returns a memory view object from a specified object.
memoryview(obj)
            obj	A Bytes object or a Bytearray object
eg: x = memoryview(b"Hello")
    print(x)
    #return the Unicode of the first character
    print(x[0])
    #return the Unicode of the second character
    print(x[1])--> <memory at 0x148defb30a00> 72 101

43.min()
The min() function returns the item with the lowest value, or the item with the lowest value in an iterable
min(n1, n2, n3, ...) --n1, n2, n3, ...	One or more items to compare
min(iterable)-- iterable	An iterable, with one or more items to compare
eg: x = min(5, 10)
    print(x)-->5
    x = min("Mike", "John", "Vicky")
    print(x)-->john

44.next()
The next() function returns the next item in an iterator
You can add a default return value, to return if the iterable has reached to its end
next(iterable, default)
                    iterable	Required. An iterable object.
                    default	Optional. An default value to return if the iterable has reached to its end
eg: mylist = iter(["apple", "banana", "cherry"])
    x = next(mylist)
    print(x)
    x = next(mylist)
    print(x)
    x = next(mylist)
    print(x)-->apple banana cherry

45.object()
The object() function returns an empty object
You cannot add new properties or methods to this object
This object is the base for all classes, it holds the built-in properties and methods which are default for all classes.
eg: x = object()
    print(dir(x))-->['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', 
                     '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
                     '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

46.oct()
The oct() function converts an integer into an octal string.
Octal strings in Python are prefixed with 0o
oct(int)
eg: x = oct(12)
    print(x)-->0o14

47.open()
The open() function opens a file, and returns it as a file object
open(file, mode)
            file	The path and name of the file
            mode	A string, define which mode you want to open the file in:
                    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
                    "a" - Append - Opens a file for appending, creates the file if it does not exist
                    "w" - Write - Opens a file for writing, creates the file if it does not exist
                    "x" - Create - Creates the specified file, returns an error if the file exist
                    "t" - Text - Default value. Text mode
                    "b" - Binary - Binary mode (e.g. images)

eg: f = open("demofile.txt", "r")
    print(f.read())-->Hello! Welcome to demofile.txt
                      This file is for testing purposes.
                      Good Luck!

48.ord()
The ord() function returns the number representing the unicode code of a specified character.
ord(character)
            character	String, any character
Convert back to character with the chr() function.

49.pow()
The pow() function returns the value of x to the power of y (xy).
If a third parameter is present, it returns x to the power of y, modulus z.
pow(x, y, z)
            x	A number, the base
            y	A number, the exponent
            z	Optional. A number, the modulus
eg: Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
    x = pow(4, 3)--> 64
    x = pow(4, 3, 5) #Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5)
    print(x)-->5

50.print()
The print() function prints the specified message to the screen, or other standard output device
The message can be a string, or any other object, the object will be converted into a string before written to the screen
print(object(s), sep=separator, end=end, file=file, flush=flush)
                                                            object(s)	Any object, and as many as you like. Will be converted to string before printed
                                                            sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
                                                            end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed)
                                                            file	Optional. An object with a write method. Default is sys.stdout
                                                            flush	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False
eg: print("Hello World")-->hello world
    print("Hello", "how are you?", sep="---")-->Hello---how are you?

51.property()
property()	Gets, sets, deletes a property
            fget is a function for getting an attribute value
            fset is a function for setting an attribute value
            fdel is a function for deleting an attribute value
eg: class C:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")--> <property object at 0x2b90cdc756d0>

52.range()
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
range(start, stop, step)
                        start	Optional. An integer number specifying at which position to start. Default is 0
                        stop	Required. An integer number specifying at which position to stop (not included).
                        step	Optional. An integer number specifying the incrementation. Default is 1
eg: x = range(3, 20, 2)
    for n in x:
    print(n)-->3 5 7 9 11 13 15 17 19

53.repr()
Returns a readable version of an object
eg: class Car:
    pass
    repr(Car())--> <__main__.Car object at 0x000001F66D11DBE0>'

    
54.reversed()
The reversed() function returns a reversed iterator object.
reversed(sequence)
eg: alph = ["a", "b", "c", "d"]
    alph = reversed(alph)
    for x in ralph:
    print(x)-->d c b a

55.round()
The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
The default number of decimals is 0, meaning that the function will return the nearest integer
round(number, digits)
            number	Required. The number to be rounded
            digits	Optional. The number of decimals to use when rounding the number. Default is 0
eg: x = round(5.76543)
    print(x)--> 6
    x = round(5.76543, 2)
    print(x)-->5.77


56.set()
The set() function creates a set object
The items in a set list are unordered, so it will appear in random order
set(iterable) iterable	Optional. A sequence, collection or an iterator object
eg: x = set(("apple", "banana", "cherry"))
    print(x)--> {'banana', 'apple', 'cherry'}

57.setattr()
The setattr() function sets the value of the specified attribute of the specified object.
setattr(object, attribute, value)
                                object	Required. An object.
                                attribute	Required. The name of the attribute you want to set
                                value	Required. The value you want to give the specified attribute
eg: class Person:
  name = "John"
  age = 36
  country = "Norway"
  setattr(Person, 'age', 40)
  # The age property will now have the value: 40
  x = getattr(Person, 'age')
  print(x)--> 40
The delattr() function, to remove an attribute
The getattr() function, to get the value of an attribute
The hasattr() function, to check if an attribute exist

58.slice()
The slice() function returns a slice object
You can specify where to start the slicing, and where to end
slice(start, end, step)
                        start	Optional. An integer number specifying at which position to start the slicing. Default is 0
                        end	An integer number specifying at which position to end the slicing
                        step	Optional. An integer number specifying the step of the slicing. Default is 1
eg: a = ("a", "b", "c", "d", "e", "f", "g", "h")
    x = slice(3, 5)
    print(a[x])-->('d', 'e')
    a = ("a", "b", "c", "d", "e", "f", "g", "h")
    x = slice(0, 8, 3)
    print(a[x])--> ('a', 'd', 'g')

59.sorted()
The sorted() function returns a sorted list of the specified iterable object.
You can specify ascending or descending order.
Strings are sorted alphabetically, and numbers are sorted numerically
sorted(iterable, key=key, reverse=reverse)
                                    iterable	Required. The sequence to sort, list, dictionary, tuple etc.
                                    key	Optional. A Function to execute to decide the order. Default is None
                                    reverse	Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
eg: Sort ascending:
    a = ("h", "b", "a", "c", "f", "d", "e", "g")
    x = sorted(a)
    print(x)-->>['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    Sort descending:
    a = ("h", "b", "a", "c", "f", "d", "e", "g")
    x = sorted(a, reverse=True)
    print(x)-->['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

60.staticmethod()
Converts a method into a static method

61.str()
The str() function converts the specified value into a string
str(object, encoding=encoding, errors=errors) 
                                            object	Any object. Specifies the object to convert into a string
                                            encoding	The encoding of the object. Default is UTF-8
                                            errors	Specifies what to do if the decoding fail
eg:x = str("12")-->12

62.sum()
The sum() function returns a number, the sum of all items in an iterable
sum(iterable, start)
                    iterable	Required. The sequence to sum
                    start	Optional. A value that is added to the return value
eg: a = (1, 2, 3, 4, 5)
    x = sum(a)--> 15
    a = (1, 2, 3, 4, 5)
    x = sum(a, 7)
    print(x)--> 22

63.super()
The super() function is used to give access to methods and properties of a parent or sibling class.
The super() function returns an object that represents the parent class.
eg: class Parent:
    def __init__(self, txt):
       self.message = txt
    def printmessage(self):
       print(self.message)
    class Child(Parent):
       def __init__(self, txt):
    super().__init__(txt)
    x = Child("Hello, and welcome!")
    x.printmessage()-->Hello, and welcome!

64.tuple()
The tuple() function creates a tuple object
tuple(iterable)
            iterable Optional. A sequence, collection or an iterator object
eg: x = tuple(("apple", "banana", "cherry"))
    print(x)-->('banana', 'cherry', 'apple') 

65.type()
The type() function returns the type of the specified object
type(object, bases, dict)
                        object	Required. If only one parameter is specified, the type() function returns the type of this object
                        bases	Optional. Specifies the base classes
                        dict	Optional. Specifies the namespace with the definition for the class
eg: a = ('apple', 'banana', 'cherry')
    b = "Hello World"
    c = 33
    x = type(a)
    y = type(b)
    z = type(c)--> <class 'tuple'> <class 'str'> <class 'int'>

66.vars()
The vars() function returns the __dict__ attribute of an object.
The __dict__ attribute is a dictionary containing the object's changeable attributes
vars(object)
            object	Any object with a __dict__attribute
Return the __dict__ atribute of an object called Person
eg: class Person:
    name = "John"
    age = 36
    country = "norway"
    x = vars(Person)
    print(x)-->{'__module__': '__main__', 'name': 'John', 'age': 36, 'country': 'norway', '__dict__': <attribute '__dict__' of 'Person' objects>, 
                '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

67.zip()
The zip() function returns a zip object, which is an iterator of tuples where the first item 
in each passed iterator is paired together, and then the second item in each passed iterator are paired together 
If the passed iterators have different lengths, the iterator 
with the least items decides the length of the new iterator
zip(iterator1, iterator2, iterator3 ...)
                                zip(iterator1, iterator2, iterator3...)Iterator objects that will be joined together
eg: a = ("John", "Charles", "Mike")
    b = ("Jenny", "Christy", "Monica", "Vicky")
    x = zip(a, b)
    #use the tuple() function to display a readable version of the result:
    print(tuple(x))--> (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))"""

with open("buildin.txt",'a') as f:
    f.write(text)
    f.close()
