Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"bharani","year":2026,"month":7}
print(a)
{'name': 'bharani', 'year': 2026, 'month': 7}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['bharani', 2026, 7])
a.items()
dict_items([('name', 'bharani'), ('year', 2026), ('month', 7)])
b={"name","year"}
type(b)
<class 'set'>
#update
a={"name":"bharani","year":2026,"month":"july"}
print(a)
{'name': 'bharani', 'year': 2026, 'month': 'july'}
a.update({"time":2})
a
{'name': 'bharani', 'year': 2026, 'month': 'july', 'time': 2}
a.update({"time":2}),
(None,)
a.update({"time":2}),({"day":"tue"})
(None, {'day': 'tue'})
a.update({"time":2,"day":"tue"})
a
{'name': 'bharani', 'year': 2026, 'month': 'july', 'time': 2, 'day': 'tue'}
#setdefault
a={"name":"bharani","city":"vij"}
>>> a.setdeafult("mali
...              
SyntaxError: unterminated string literal (detected at line 1)
>>> a.setdeafult("mali","bharani@nandam.com")
...              
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.setdeafult("mali","bharani@nandam.com")
AttributeError: 'dict' object has no attribute 'setdeafult'. Did you mean: 'setdefault'?
>>> a.setdeafult("mali","bharani@gmail.com")
...              
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.setdeafult("mali","bharani@gmail.com")
AttributeError: 'dict' object has no attribute 'setdeafult'. Did you mean: 'setdefault'?
>>> a
...              
{'name': 'bharani', 'city': 'vij'}
>>> a.setdefault("mali","bharani@gmail.com")
...              
'bharani@gmail.com'
>>> a
...              
{'name': 'bharani', 'city': 'vij', 'mali': 'bharani@gmail.com'}
