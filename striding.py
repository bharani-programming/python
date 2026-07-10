Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
a="data science"
a[::]
'data science'
a[:]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
a[::4]
'd e'
a=machine learning
SyntaxError: invalid syntax
a="machine learning"
a[::4]
'miln'
>>> a[::7]
'm n'
>>> a[::2]
'mcielann'
>>> a[2:8]
'chine '
>>> a[:9]
'machine l'
>>> a[7:]
' learning'
>>> a="cloud computing"
>>> a[1:12:3]
'ldou'
>>> a[-4:-14:-4]
'tou'
>>> a[-6:-10:-1]
'pmoc'
>>>  a[-2:-13:-5]
...  
SyntaxError: unexpected indent
>>> a[-2:-13:-5]
'nmu'
>>> a="cloud computing"
>>> [4:14:4]
SyntaxError: invalid syntax
>>> a[4:14:4]
'dmi'
a[6:0:1]
''
a[6:10:1]
'comp'
a[2:13:5]
'ooi'
