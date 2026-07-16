Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #pop
>>> a={"state":"ap","country":"india"}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop("country")
'india'
>>> a
{'state': 'ap'}
>>> a.popitem()
('state', 'ap')
>>> a
{}
>>> #copy
>>> a={"colour":"black","food":"biryani"}
>>> a.copy()
{'colour': 'black', 'food': 'biryani'}
>>> b=a.copy()
>>> b
{'colour': 'black', 'food': 'biryani'}
>>> len(a)
2
>>> a={"name":"bharani","city":"vij","name":"pooja"}
>>> print(a)
{'name': 'pooja', 'city': 'vij'}
a={"name":"bharani","city":"vij","name":"pooja"}
a
{'name': 'pooja', 'city': 'vij'}
a={"name1":"bharani","city":"vij","name2":"pooja"}
a
{'name1': 'bharani', 'city': 'vij', 'name2': 'pooja'}
a.count(name1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.count(name1)
AttributeError: 'dict' object has no attribute 'count'
a={"name":"bharani","city":"vij","name":"pooja"}
a.count(name)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.count(name)
AttributeError: 'dict' object has no attribute 'count'
a.index("city")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.index("city")
AttributeError: 'dict' object has no attribute 'index'
a.count("name")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
a.clear()
a
{}
b={}
b.update({"name":"pooja"})
b
{'name': 'pooja'}
a=
SyntaxError: invalid syntax
a={"idnos":[10,20,30],"names":["sai","kiran","basha"],"mark":[60,70,80]}
print(a)
{'idnos': [10, 20, 30], 'names': ['sai', 'kiran', 'basha'], 'mark': [60, 70, 80]}
