Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes coversations
#int
int(3)
3
int(9.8)
9
int("hi")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(5+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(5+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(4.8)
4.8
float(9)
9.0
float("hello")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("hello")
ValueError: could not convert string to float: 'hello'
float(4+7j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(4+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#str()
str(5)
'5'
str(7.8)
'7.8'
str("python")
'python'
str(6+9j)
'(6+9j)'
str(True)
'True'
str(False)
'False'
#complex
>>> complex(4)
(4+0j)
>>> complex(6.7)
(6.7+0j)
>>> complex(7+8j)
(7+8j)
>>> complex(True)
(1+0j)
>>> complex(false)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> complex(False)
0j
>>> #bool
>>> bool(8)
True
>>> bool(7.9)
True
>>> bool(6+8j)
True
>>> bool(True)
True
>>> bool(False)
False
