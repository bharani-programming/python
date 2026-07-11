Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#len
a="codegnan"
len(a)
8
b="nandam bharani"
len(b)
14
c="i love python"
len(c)
13
d=""
len(d)
0
e=" "
len(e)
1
#count()
a="twinkle twinkle little start"
a.count(a)
1
a.count(l)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.count(l)
NameError: name 'l' is not defined
a.count("l")
4
a.count("e")
3
a.count("a")
1
a.count("twinkle")
2
#find a string
a="python"
a.find("n")
5
a.find("python")
0
b="hello"
a.find("l")
-1
b.find("l")
2
# escape sequences
#\n->new line
#\t->tab space
a="name\nmailid\tmobileno\ncollege\tbranch"
print(a)
name
mailid	mobileno
college	branch
a
'name\nmailid\tmobileno\ncollege\tbranch'
a="name:bharani\nmailid:nandambharani@gmail.com\tmobileno:9381042690\ncollege:s.d.m.s.m.k\tbranch:computer science"
print(a)
name:bharani
mailid:nandambharani@gmail.com	mobileno:9381042690
college:s.d.m.s.m.k	branch:computer science
a="name:bharani\nmailid:nandambharani@gmail.com\nmobileno:9381042690\ncollege:s.d.m.s.m.k\nbranch:computer science"
print(a)
name:bharani
mailid:nandambharani@gmail.com
mobileno:9381042690
college:s.d.m.s.m.k
branch:computer science
#replace
a="wait until you  suceed"
a.replace("wait","work")
'work until you  suceed'
b="python"
b.replace("t","i")
'pyihon'
c="twinkle twinkle little start"
c.replace("twinkle","two")
'two two little start'
c.replace("twinkle","two",1)
'two twinkle little start'
c.replace("t","o")
'owinkle owinkle lioole soaro'
#upper()
a="code"
a.upper()
'CODE'
b="code"
b.lower()
'code'
a="code"
a.upper()
'CODE'
#lower()
c="HELLO"
c.upper()
'HELLO'
c.lower()
'hello'
d="python"
c.upper[p]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    c.upper[p]
NameError: name 'p' is not defined
d.upper[p]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    d.upper[p]
NameError: name 'p' is not defined
d[0].upper()
'P'
c.capitalize()
'Hello'
d.capitalize()
'Python'
d.tittle()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    d.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
e="nandam bharani"
e.tittle()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    e.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
e.title()
'Nandam Bharani'
a="bharani"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True

a="nandam bharani"
a.isupper()
False
a.islower()
True
a.isalpha()
False
b=("1223456")
b.isupper()
False
b.isdigit()
True
b=("1223456,23456789")
b.isdigit()
False
b.isupper()
False
b.islower()
False
a="bharani93810"
a.isalnum()
True
b="bharani#5698"
b.isalnum
<built-in method isalnum of str object at 0x0000029F4763B370>
b="bharani@5698"
b.isalnum()
False
a="bharani"
a.startwith("b")
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.startwith("b")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith("b")
True
a.endswith("i")
True
a.startswith("u")
False
a.endswith("a")
False
#strip
#strip()
#lstrip(),#rstrip()
a="     bharani   "
a.strip()
'bharani'
a.lstrip()
'bharani   '
a.rstrip()
'     bharani'
a="you need a more specific answer"
a.strip()
'you need a more specific answer'
a.lstrip()
'you need a more specific answer'
a.rstrip()
'you need a more specific answer'
#split
a=("python java c++")
a.split()
['python', 'java', 'c++']
b="trainee at codegnan"
b.split()
['trainee', 'at', 'codegnan']
#join()
b="html","css","js","python"
"    ".join(b)
'html    css    js    python'
"".join(b)
'htmlcssjspython'
"  ".join(b)
'html  css  js  python'
" b ".join(b)
'html b css b js b python'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="coffee"
b="tea"
print(a+b)
coffeetea
print(a+" "+b)
coffee tea
fname="bharani"
lname="nandam"
print(("fname+lname").title())
Fname+Lname
print(fname+lname)
bharaninandam
print(fname+" "+lname)
bharani nandam
print((fname+" "+lname).title())
Bharani Nandam
print(fname.title()+" "+lname.title())
Bharani Nandam
#formatting
a=7
b=7
print(a+b)
14
print("thesumis",a+b)
thesumis 14
print("thesumis"a+b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("the sum is",a-b)
the sum is 0
city="vijayawada"
print("city is ",city)
city is  vijayawada
a=0
b=87
print("the sum is",a*b)
the sum is 0
print("the mul is",a/b)
the mul is 0.0
#format()
a="motu"
b="pathulu"
print("hello {} {}".format(a,b))
hello motu pathulu
print("hi {}{}".format(a,b))
hi motupathulu
print("hi {} hi {}".format(a,b))
hi motu hi pathulu
print("hi {}\nhi {}".format(a,b))
hi motu
hi pathulu
print("hi\n how are you {}\nhi\n how are you {}".format(a,b))
hi
 how are you motu
hi
 how are you pathulu
print("hi motu \nhow are you {}\nhi pathulu\n how are you {}".format(a,b))
hi motu 
how are you motu
hi pathulu
 how are you pathulu

>>> print("hi motu \nhow are you {}\nhi pathulu\nhow are you {}".format(a,b))
hi motu 
how are you motu
hi pathulu
how are you pathulu
>>> #fstring
>>> a="bharani"
>>> b="chinni"
>>> print(f"hello {a}{b}")
hello bharanichinni
>>> print(f"hello {a} {b}")
hello bharani chinni
>>> print(f"hello {a} hello {b}")
hello bharani hello chinni
>>> print(f"\nhello {a}\nhello {b}")

hello bharani
hello chinni
>>> print(f"hello {a}\nhello {b}")
hello bharani
hello chinni
>>> print(f"hello \nwhat are you doing now {a}\nhello\nwhat are you doing now {b}")
hello 
what are you doing now bharani
hello
what are you doing now chinni
