Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #arthematic operators
>>> a=9
>>> b=8
>>> print(a+b)D
17
>>> a=65
>>> b=76
>>> print(a-b)
-11
>>> a=5
>>> b=6
>>> print(a*b)
30
>>> print(a%b)
5
>>> print(a**b)
15625
>>> print(a//b)
0
>>> print(a/b)
0.8333333333333334
>>> #assginment
>>> a=5
>>> b=3
a+=b
b
3
b-=a
b
-5
b*=4
b
-20
b%=7
b
1
b**=6
b
1
b//=6
b
0
b/=9
b
0.0
a=7
b=8
a+=b
a
15
a-=b
a
7
a*=7
a
49
a%=b
a
1
a//=b
a
0
a/=b
a
0.0
#comparision
a=8
b=6
a<b
False
a>b
True
a<=b
False
a>=b
True
a!=b
True
a==b
False
a=7.8
b=9.8
a<b
True
a>b
False
a<=b
True
a>=b
False
a!=b
True
a==b
False
#logical
a=4
b=6
a<b and a>b
False
a>b and a<b
False
a!=b and a==b
False
a==b or a!=b
True
not true
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
#identify operator
a=11
b=12
type(a) is int
True
type(a) is not int
False
b=7.6
type(b) is float
True
type(b) is not float
False
x="bharani"
type(x) is str
True
type(x) is not str
False
y=6+8j
type(y) is complex
True
type(y) is not complex
False
a= True
type(a) is bool
True
b=False
type(b) is not bool
False
#membership
a=2,3,4,5,6,7,8,9
9 in a
True
9 not in a
False
11 in a
False
11 not in a
True
a= "python","c++"
"python","c++" in a
('python', True)
#btwise operator
a=8
b=7
a&b
0
bin(8)
'0b1000'
bin(7)
'0b111'
a= 5
b=1
a&b
1
a=3
b=8
a&b
0
bin(a)
'0b11'
bin(b)
'0b1000'
(OR)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    (OR)
NameError: name 'OR' is not defined
a=5
b=9
a/b
0.5555555555555556
a|b
13
a=2
b=6
a|b
6
d=6
e=7
6~7
SyntaxError: invalid syntax

































































































































+
a=6
a~
SyntaxError: invalid syntax
~a
-7
a=6
-(a+1)
-7
b=12
-(a+1)
-7
~b
-13
#xor
a=7
b=5
a^b
2
a=1
b=7
a^b
6
a="python"
b="c"
a^b
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    a^b
TypeError: unsupported operand type(s) for ^: 'str' and 'str'
a=8
b=10
a^b
2
a=6<<3
a=4
a>>2
1
a=3
a>>3
0
a=4
a<<2
16

