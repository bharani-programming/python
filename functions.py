'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

#FUNCTIONS
#def keywords

'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#**,%,//

'''def calculate(c,d):
    print("the sum is",c**d)
    print("the diff is",c%d)
    print("the product is",c//d)
calculate(2,2)
calculate(12,6)
calculate(14,5)'''

'''def add(a,b):
    print(a+b)
add(4,9)'''
#run time
'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a*b)
    add()'''
#recursion()
    
'''def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a*b)
        add()
add()'''
'''def fullname():
    fname=input("enter a name")
    lname=input("enter a name")
    print(fname+" "+lname)
fullname()'''   
#PRINT V/S RETURN
'''def mul(a,b):
    print(a*b)
mul(4,5)'''

'''def mul(a,b):
    return a*b
print(mul(4,6))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
 cal(5,6)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    #return(c)
    #return(d)
    return c,d
print(cal(5,6))'''

'''def num():
    a=int(input("a value:"))
    b=int(input("b value:"))
    c=int(input(choose options
                 1.add
                 2.sub
                 3.mul))
    if c==1:
        print("the sum is",a+b)
    elif c==2:
         print("the diff is",a-b)
    elif c==3:
          print("the mul is",a*b)
    num()
num()'''
#method 2
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:    
    a=int(input("a value:"))
    b=int(input("b value:"))
    c=int(input(choose options
                     1.add
                     2.sub
                     3.mul))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        mul()'''
#keyword and positional arguments
#step 1
'''def Details(id,name,mailid):
    id=10
    name="bharani"
    mailid="b@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''    

#step 2    
'''def Details(id,name,mailid):    
    print(id,name,mailid)
Details(id=20,name="chinni",mailid="c@gmail.com")
Details(id=30,name="nani",mailid="n@gmail.com")'''
               
#step 3
'''def Details(id,name,mailid):    
    print(id,name,mailid)
Details(40,"lalitha","l@gmail.com")'''
#step 4
'''def Details(id,name,mailid):    
    print(id,name,mailid)
Details("kishore","k@gmail.com",50)'''
#step 5
'''def Details(id,name,mailid):    
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")   
Details(name="nani",mailid="n@gmail.com",id=60)'''

'''def Details(id,name,mailid):    
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=10,name="nanna",mailid="na@gmail.com")
Details(id=20,name="chinni",mailid="c@gmail.com")
Details(id=30,name="nani",mailid="n@gmail.com")            
Details(40,"lalitha","l@gmail.com")
Details("kishore","k@gmail.com",50)
Details(name="nani",mailid="n@gmail.com",id=60)'''

#default arguments
#step 1
'''def Grocery(item,price,quantity):
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
Grocery("rice",1600,12)'''
#step 2
'''def Grocery(item="chicken",price=280,quantity=2):
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
Grocery()'''
#step 3
'''def Grocery(item,price=280,quantity=2):
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
Grocery("briyani")'''
#step 4
'''def Grocery(item="ghee",price,quantity):
    #non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
Grocery(1200)'''

#cake,price,quantity
#step 1
'''def bakery(cake,price,quantity):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
bakery("vennala",1200,"1kg")'''
#step 2
'''def bakery(cake="chocalate",price=3000,quantity="2kg"):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
bakery()'''
#step 3
'''def bakery(cake,price=2000,quantity="3kg"):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
bakery("pineapple")'''

'''def bakery(cake,price,quantity="3kg"):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
bakery("pineapple",4000)'''
#step 4
'''def bakery(cake="chocalate",price,quantity):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
bakery(2500,"4kg")'''
#*arguments(* is used to unpack the elements & mutlipe data)
'''a=[10,20,30,40,50]
print(a)
print(*a)

a=(10,20,30,40,50)
print(a)
print(*a)

a={10,20,30,40,50}
print(a)
print(*a)

a={"years":2026,"month":"july"}
print(a)
print(*a)'''

'''a,b,c=2,3,4,6,7,8,9
print(a)'''

'''a,b,c=2,3,4
print(a)
print(b)
print(c)

*a,b,c=2,3,4,6,7,8,9
print(*a)
print(b)
print(c)

a,*b,c=2,3,4,6,7,8,9
print(a)
print(*b)
print(c)

a,b,c="bharani"
print(a)
print(b)
print(c)

*a,b,c="bharani"
print(*a)
print(b)
print(c)

a,*b,c="bharani"
print(a)
print(*b)
print(c)'''

#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,6,7,)
b=[4,5,6,7,8]
check(*b)
c={5,9,6,3,4}
check(*c)
d={"name":"chinni","city":"vij"}
check(*d)'''

'''def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
           d=d+i
           print(d)
check1()
check1(2,4,6,8,9)
check1(4,5,7,9.2,6.7)
check1(3,4,5,6.5,3.5,"bharani",5+9j,True,False)'''

#kwargs(**)
'''def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
check(**details)

def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
check(**details)'''
        
#both * and ** usage
'''def final(*a,**b):
    d=4#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("keys is",i)
        print("values is",j)
final()
data=(2,4,5.8,9.6)
final(*data)
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
final(**details)
final(*data,**details)'''

#max(),min(),sum()
'''print(max(5,4,6,9,12))
print(min(5,4,6,9,12))
s=5,4,6,9,12
print(sum(s))'''

#marks analaysis report
'''n = int(input("Enter number of students: "))
total = 0
highest = 0
lowest = 100
for i in range(n):
    marks = int(input("Enter marks: "))
    total = total + marks
    if marks > highest:
        highest = marks
    if marks < lowest:
        lowest = marks
average = total / n
print("\n.........Marks Analysis Report............")
print("Total Students :", n)
print("Highest Marks  :", highest)
print("Lowest Marks   :", lowest)
print("Total Marks    :", total)
print("Average Marks  :", average)'''



'''n=int(input("enter no.of students"))
marks=[]
for i in range(1,n+1):
      mark=int(input(f"enter the student{i} marks"))
      marks.append(mark)
for i in marks:
      print(i)
print("\n.........Marks Analysis Report............")
print("Total Students ", n)
print("Highest Marks  ", max(marks))
print("Lowest Marks   ", min(marks))
print("Total Marks    ", sum(marks))
print("Average Marks  ",sum(marks)/n) '''

#global and local variables
#first case of global variable
'''a=2
def check1():
    print("the inside value is",a)
check1()
print("outside value is",a)'''

#second case of global variable
'''a=4
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''

#third case both global and local variable
'''a=8
b=4
def check3():
    a=6
    print("inside value is",a)
    a=10
    print("updated value is",a+6)
    b=5
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)'''

#fourth case usage of global key word #scope of the variables topic
#when user wants to create a variable inside the function directly
#and carry forward the updated value and then we can use the global variable
'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=20
    print("updated value is",a+6)
    b=15
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''
#generators
#definination:no tuple comprehension in above cases if we those braces
#and keep parantheses then the outcome is genereted
#a=[expr for var in collection/range]
#list comprehensions
'''a=[i for i in range(16)]
print(a)
print(type(a))'''
#generators
'''a=(i for i in range(16))
print(*a)
print(type(a))'''

'''a=[i for i in range(16)]
#print(list(a))
#print(tuple(a))
print(set(a))'''
#a genertor is also a function which can be use an in iteration (loop) by producing of
#group of values where we can use yield keyword

#yield VS return
#return terminate the fun where as yield can pass the fun()
#and go on with every sucessive iteration
'''a,b=(int(x) for x in  input("value").split(","))
def check(a,b):
    while a<b:
        yield a
        a=a+2
        yield a
print(*check(a,b))'''

'''a,b=(int(x) for x in  input("value").split(","))
def check(a,b):
    while a<b:
        a=a+2
        return a
print(check(a,b))'''

#yield/return
'''def mygen():
    #return "vja"
    #return "hyd"
    #return "vzg"
    return "vja","hyd","vzg"
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "c"
print(*mygen())

#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))#stop iteration'''

#print(),input(),max(),min(),sum(),len(),type(),range(),pow()
'''a=2
print(a)

n=int(input("enter a value"))
print(n)

print(max(5,4,6,9,12))
print(min(5,4,6,9,12))
s=5,4,6,9,12
print(sum(s))

a="python"
print(len(a))

a=5.6
print(type(a))
print(a)

for i in range(0,5):
    print(i)
    
a=2
print(a*2)'''

#print(dir())
#print(dir("__builtins__"))
#from keys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))      
print(set(a))
#print(dict(a))

b=dict.fromkeys(a)
print(b)
c=dict.fromkeys(a,"chinni")
print(c)
c["o"]="bharani"
print(c)
c["c"]="potti"
print(c)
c["d"]="c"
print(c)
c["e"]="html"
print(c)'''
 
#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''    
    
'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b) '''
#zip->we can combine multiple collections into one collection
'''a=[10,20,30,40,50,60]
names=["bharani","harsha","tambii","dikshi","vaishu","nani"]
print(a+names)

b=zip(a,names)
print(b)
c=list(zip(a,names))
print(c)
d=tuple(zip(a,names))
print(d)
e=set(zip(a,names))
print(e)
f=dict(zip(a,names))
print(f)
g=list(zip(a,names))
print(*g)'''
#enumerate()->we can give counter to the collection
names=["bharani","chinni","nani","nc"]
'''for i in range(len(names)):
    print(i, names[i])'''
'''b=dict(enumerate(names))
print(b)
b=dict(enumerate(names,10))
print(b)
c=set(enumerate(names,10))
print(c)
c=tuple(enumerate(names,10))
print(c)
c=list(enumerate(names,10))
print(c)'''
#railway ticket
while True:
    def raliway_ticket():
        ticket=1000
        gender=input("Choose gender (male/female): ").lower()   
        age=int(input("Enter Age: "))
        if gender=="m":
           if age > 60:
               print("senior citizen")
               ticket=ticket- (ticket * 30 / 100)
               print(ticket)
           elif age<60:
               print("noraml citizen")
               print(ticket)
        elif gender=="f":
            if age >= 60:
               print("senior citizen")
               ticket=ticket- (ticket * 30 / 100)
               print(ticket)
            elif age<60:
                  print("normal citizen")
                  ticket=ticket- (ticket * 50 / 100)
                  print(ticket)
raliway_ticket()   

#annonymous functions
#annonymous are names function and we use a keyword called as lambda to create annonymous()
#write afunction to calculate 2*x+5 where x=5
'''def calculate_expression(x):
    return 2 * x + 5
result = calculate_expression(5)
print(result)

def f(x):
    print(2 * x + 5)
f(5)'''

'''def f():
    x=int(input("value"))
    print(2*x+5)
f()'''    

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))'''

'''a="codegnan"
#CODEGNAN
b=lambda a:a.upper()
print(b(a))

a="python course"
#Python Course
b=lambda a:a.title()
print(b(a))'''

#multiply
'''a=2 
b=3
c=lambda a,b:a*b
print(c(a,b))
      (or)
c=lambda a,b:a*b
print(c(5,6))

a=int(input("a value"))
b=int(input("b value"))
c=lambda a,b:a*b
print(c(a,b))'''

'''a=input("first name")
b=input("last name")
c=lambda a,b:a+b
print(c(a,b))'''

'''def name_generator(first_name, last_name):
    yield f"{first_name} {last_name}"
full_name_gen = name_generator("Bharani", "Nandam")
print(next(full_name_gen))'''

'''a,b=[x for x in input("enter the names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter()
a=[10,20,30,40,55,32,33,77]
'''if a%2==0:
    print(a)'''

'''for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

#[],(),{}
'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''

'''a=[[],{},(),None," ",2,3.5,"python",5+6j,True,False]
b=list(filter(None,a))
print(b)'''

#map()->each object from a collection and forms a new collection
'''a=[2,4,6,79,4,20,35]
b=[30,21,45,9,13,56,60]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)
d=map(min,a,b)
print(d)'''










