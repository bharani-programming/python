Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a="codegnan"
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> a[2:]
'degnan'
>>> a[0:]
'codegnan'
>>> a[:9]
'codegnan'
>>> a="work until you succeed"
>>> a[0:]
'work until you succeed'
>>> a[0:4]
'work'
>>> a[5:10]
'until'
>>> a[15:21]
'succee'
>>> a[15:]
'succeed'
>>> a[11:14]
'you'
b="time is very precious"
b[13:]
'precious'
b[8:12]
'very'
b[:5]
'time '
b[0:]
'time is very precious'
b[13:21]
'precious'
a= "simple is better than complex
SyntaxError: unterminated string literal (detected at line 1)
a= "simple is better than complex"
a[-19:-13]
'better'
a[-29:-23]
'simple'
a[-7:0]
''
a[-8:]
' complex'
a[-7:-0]
''
a[-7:]
'complex'
a= "codegnan it solutions"
a[-9:]
'solutions'
a[-10:-1]
' solution'
a[-9:-1]
'solution'
