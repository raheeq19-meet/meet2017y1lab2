Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> >>> a = 5
>>> b = 10
>>> c = a
>>> a = b
>>> b = c
>>> a
10
>>> b
5
>>> c
5
>>> four = '4'
>>> print(four*3)
444
>>> five = 4
>>> print(five)
4
>>> print(five*3)
12
>>> my_name = 'student'
>>> print("hi," = myname')
      
SyntaxError: EOL while scanning string literal
>>> my_name = 'student'
>>> print("Hi,"+ my_name)
Hi,student
>>> my_age = 15
>>> print('I am' + my_age + 'years old')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print('I am' + my_age + 'years old')
TypeError: Can't convert 'int' object to str implicitly
>>> my_age = '15'
>>> print('I am' + my_age + 'years old')
I am15years old
>>> my_age = '15'
>>> print('I am ' + my_age + ' years old')
I am 15 years old
>>> score = 1
>>> total = score + (count*2)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    total = score + (count*2)
NameError: name 'count' is not defined
>>> score = 1
>>> count = 3
>>> total = score+(count*2)
>>> print(total)
7
