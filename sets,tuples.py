Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,4.5,"python",6+9j,True,False]
print(a)
[2, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=8.9
print(b)
8.9
c=[8.9]
type(c)
<class 'list'>
#append
a=["python","c","html"]
a.append("c++")
a
['python', 'c', 'html', 'c++']
a.append("html","css")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.append("html","css")
TypeError: list.append() takes exactly one argument (2 given)
a.append("ai","css")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.append("ai","css")
TypeError: list.append() takes exactly one argument (2 given)
a.append[("ai","css")]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.append[("ai","css")]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.append(["ai","css"])
a
['python', 'c', 'html', 'c++', ['ai', 'css']]
#extend
a=["html","css","js"]
a.extend(["python","cddd"])
a
['html', 'css', 'js', 'python', 'cddd']
#insert
b=["vij","hyd","vzg"]
b
['vij', 'hyd', 'vzg']
b.insert(3,"gudavalli")
b
['vij', 'hyd', 'vzg', 'gudavalli']
a=["apples","pineapple
   
SyntaxError: unterminated string literal (detected at line 1)
a=["apples","pineapple","grapes"]
   
a
   
['apples', 'pineapple', 'grapes']
a.index("pineapple")
   
1
a.copy()
   
['apples', 'pineapple', 'grapes']
b=a.copy()
   
a.count("grapes")
   
1
len(a)
   
3
d="apples"
   
len(d)
   
6
e="apples"
   
len(e)
   
6
a=["mango","kiwi","dragon","berry"]
   
a.sort()
   
a
   
['berry', 'dragon', 'kiwi', 'mango']
b=[4,5,68,778,5,52,0]
   
b.sort()
   
b
   
[0, 4, 5, 5, 52, 68, 778]
6
   
6
a=["ds","ai","ml"]
   
a.reverse()
   
a
   
['ml', 'ai', 'ds']
b=[23,4,4,6,8]
   
b.reverse()
   
b
   
[8, 6, 4, 4, 23]
a=["black","red","purple","white"]
   
a.pop()
   
'white'
a
   
['black', 'red', 'purple']
a.pop(3)
   
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.pop(3)
IndexError: pop index out of range
a.pop(0)
   
'black'
a
   
['red', 'purple']
a.remove("white")
   
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.remove("white")
ValueError: list.remove(x): x not in list
a.remove("red")
   
a
   
['purple']
a=["ap","ka","ts"]
   
a.clear()
   
a
   
[]
b=[]
   
b.append("pooja")
   
b
   
['pooja']
b.append("bharani")
   
b
   
['pooja', 'bharani']
a=(10,20,30,"code")
   
a.extend("code")
   
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.extend("code")
AttributeError: 'tuple' object has no attribute 'extend'
a=[10,20,30,"code"]
   
a.extend("code")
   
a
   
[10, 20, 30, 'code', 'c', 'o', 'd', 'e']

#tuple()
   
a=(4,5.6,"python",8+8j,True,False)
   
print(a)
   
(4, 5.6, 'python', (8+8j), True, False)
type(a)
   
<class 'tuple'>
a.index(8+8j)
   
3
len(a)
   
6
a.count(True)
   
1
a.count(4)
   
1
a.count(False)
   
1
#sets
   
a={4,5,6,7,8,9}
   
print(a)
   
{4, 5, 6, 7, 8, 9}
type(a)
   
<class 'set'>
b={7,8,9,6,8,7,4}
   
print(b)
   
{4, 6, 7, 8, 9}
#add
   
a={7,8,9,0,2}
   
a.add(34)
   
a
   
{0, 2, 34, 7, 8, 9}

#issubset
   
a={5,6,7,8,9}
   
b={6,7,8,9}
   
b.issubset(a)
   
True
a.issubset(b)
   
False
a={a={5,6,7,8,9}
   
SyntaxError: '{' was never closed
a={5,6,7,8,9}b={6,7,8,9}
   
SyntaxError: invalid syntax
a={6,7,8,9,45,78}
   
b={6,7,8,9}
   
a.issuperset(b)
   
True
b.issuperset(a)
   
False
#union()
   
a={3,4,5,6,7,8}
   
b={3,4,5,6,7,8,67,566,33,7799}
   
a.union(b)
   
{3, 4, 5, 6, 7, 8, 67, 33, 566, 7799}
b.union(a)
   
{33, 3, 4, 5, 6, 7, 8, 67, 566, 7799}
a.union(b)
   
{3, 4, 5, 6, 7, 8, 67, 33, 566, 7799}
a={3,4,5,6,7,8}b={3,4,5,6,7,8,67,566,33,7799}
   
SyntaxError: invalid syntax
a={3,4,5,6,7,8}b={3,4,5,6,7,8,67,566,33,7799}
   
SyntaxError: invalid syntax
a={3,4,5,6,7,8}
   
b={3,4,5,6,7,8,67,566,33,7799}
   
a.insertion(b)
   
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    a.insertion(b)
AttributeError: 'set' object has no attribute 'insertion'. Did you mean: 'intersection'?
a.intersection(b)
   
{3, 4, 5, 6, 7, 8}
b.intersection(a)
   
{3, 4, 5, 6, 7, 8}
a={3,4,5,6,7,8}
   
b={3,4,5,6,7,8,67,566,33,7799}
   
a.difference(b)
   
set()
b.difference(a)
   
{33, 67, 566, 7799}
 #update()
   
a={2,3,4,5,6,7}
   
b={{1,5,9,10}
a.update(b)
   
SyntaxError: '{' was never closed
a={2,3,4,5,6,7}
   
b={1,5,9,10}
a.update(b)
   
SyntaxError: multiple statements found while compiling a single statement
#symmertic difference
   
a={2,3,4,5,6,7}
   
b={3,4,5,6,7,8,67,566,33,7799}
   
a.symmertic_difference(b)
   
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a.symmertic_difference(b)
AttributeError: 'set' object has no attribute 'symmertic_difference'. Did you mean: 'symmetric_difference'?
a={4,5,7,80,89}
   
b={4,5,7,09,87}
   
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a={4,5,7,80,89}
   
b={4,5,7,9,87}
   
a.symmertic_difference(b)
   
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    a.symmertic_difference(b)
AttributeError: 'set' object has no attribute 'symmertic_difference'. Did you mean: 'symmetric_difference'?
b.symmertic_difference(a)
   
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    b.symmertic_difference(a)
AttributeError: 'set' object has no attribute 'symmertic_difference'. Did you mean: 'symmetric_difference'?
b.symmetric_difference(a)
   
{80, 87, 89, 9}
a={4,5,6,7,8,9}
   
b={1,2,3,4,5,6,10}
   
a.difference_update(b)
   
a
   
{7, 8, 9}
b.difference_update(a)
   
b
   
{1, 2, 3, 4, 5, 6, 10}
a={11,21,23,22}
   
b={11,21}
   
a.symmetric_difference_update(b)
   
a={3,4,5,6,7}
   
a.pop()
   
3
a
   
{4, 5, 6, 7}
a.pop(2)
   
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
a.remove(4)
   
a
   
{5, 6, 7}
a={10,20,30,40,50}
   
a.copy()
   
{50, 20, 40, 10, 30}
b=a.copy()
   
b
   
{50, 20, 40, 10, 30}
a.discard(50)
   
a
   
{20, 40, 10, 30}
a.clear()
   
a
   
set()
set()
   
set()
>>> b=set()
...    
>>> b.add(100)
...    
>>> b
...    
{100}
>>> a={2,3,4,5,6,7}
...    
>>> b={6,7,8,9,10}
...    
>>> a.isdisjoint(b)
...    
False
>>> c={10,20,30,40,50}
...    
>>> d={60,70,80,90}
...    
>>> c.disjoint(d)
...    
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    c.disjoint(d)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> c.isdisjoint(d)
...    
True
