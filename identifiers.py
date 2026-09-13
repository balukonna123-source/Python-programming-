Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name="Balu"
age=18
pi=3.14
class Text:
    pass
def greet():
...     
SyntaxError: invalid syntax
>>> def greet():
...     print("hello")
... greet()
SyntaxError: invalid syntax
>>> greet()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    greet()
NameError: name 'greet' is not defined
>>> 
>>> greet()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    greet()
NameError: name 'greet' is not defined
>>> def greet():
...     print("welcome")
... 
...     
>>> greet()
welcome
>>> print(name)
Balu
>>> print(age)
18
>>> print(pi)
3.14
>>> print(Text)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(Text)
NameError: name 'Text' is not defined. Did you mean: 'next'?
>>> class Text:
...     pass
... 
>>> print(Text)
<class '__main__.Text'>
