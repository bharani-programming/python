Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,4.5,"python",6+9j,True,False]
print(a)
[2, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=9.7
print(b)
9.7
type(b)
<class 'float'>
c=[7.9]
print(c)
[7.9]
type(c)
<class 'list'>
#append
a=["python","c","c++"]
a.append("html")
a
['python', 'c', 'c++', 'html']
a.append("ai","js")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append("ai","js")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ai","js"])
a
['python', 'c', 'c++', 'html', ['ai', 'js']]
#extend
a=["html","c","mi"]
a.extend(["python","c++"])
a
['html', 'c', 'mi', 'python', 'c++']
#insert
b=["vij","hyd","vzg"]
b
['vij', 'hyd', 'vzg']
b.insert(3,"velupur")
b
['vij', 'hyd', 'vzg', 'velupur']
a=["apples","bananas","blueberry"]
a.index("blueberry")
2
a.copy()
['apples', 'bananas', 'blueberry']
b=a.copy()
a.count("blueberry")
1
len(a)
3
c="pineapple"
len(c)
9
d="kiwi"
len(d)
4
a=["mango","kiwi","dargon","berry"]
a.sort()
a
['berry', 'dargon', 'kiwi', 'mango']
b=[2,3,4,4,5,9,10]
b.sort()
b
[2, 3, 4, 4, 5, 9, 10]
a=["ds","ts","mi"]
a.reverse()
a
['mi', 'ts', 'ds']
b=[34,5,6,9,78]
b.reverse()
b
[78, 9, 6, 5, 34]
a=["black","green","purple","red"]
a.pop()
'red'
a
['black', 'green', 'purple']
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.pop(3)
IndexError: pop index out of range
a.pop(2)
'purple'
a
['black', 'green']
a.remove("purple")
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.remove("purple")
ValueError: list.remove(x): x not in list
a.remove("green")
a
['black']
>>> a=["ap","ka","ts"]
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("pooja")
>>> b
['pooja']
>>> b.appened("bharani")
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    b.appened("bharani")
AttributeError: 'list' object has no attribute 'appened'. Did you mean: 'append'?
>>> b.append("Bharani")
>>> b
['pooja', 'Bharani']
>>> b.append
<built-in method append of list object at 0x0000028FE1C948C0>
>>> b.append("chinni")
>>> b
['pooja', 'Bharani', 'chinni']
>>> a=[10,20,30,40,"code"]
>>> a.extend("code")
>>> a
[10, 20, 30, 40, 'code', 'c', 'o', 'd', 'e']
