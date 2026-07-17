#if-condition by using comparision opeartors
#<,>,<=,>=,!=,==
'''a=10
b=15
if a<b:
    print("true")'''

'''a=6
b=9
if a>b:
    print("true")'''

'''a=12
b=34
if a<=b:
    print("true")'''

'''a=10
b=15
if a>=b:
    print("true")'''

'''a=15
b=15
if a==b:
    print("true")'''

'''a=10
b=15
if a!=b:
    print("not equal")'''

'''a=9
if a>3:
    print("less")'''

'''a=15
b=15
if a==b:
    print("equal")'''

'''a="python"
if a=="python":
    print("equal")'''

'''a="python"
if a!="java":
    print(" not equal")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
      print("less")'''

'''a=int(input("a value"))
if a>10:
      print("less")'''

'''a=input("data:")
if a=="python":
      print("equal")'''
#if-conditional by using logical operators
#and,or,not
'''a=5
b=7
if a<b and b>a:
    print("true")'''
'''a=4
b=6
if a<=b and b>=a:
    print("true")'''

'''a=4
b=7
if a!=b and a==b:
    print("true")'''

'''a=3
b=1
if a<=b or b>=a:
    print("true")'''
'''a=3
b=1
if a<b or b>a:
    print("true")'''
'''a=30
b=10
if a!=b or b!=a:
    print("true")'''
'''a=5
b=9
if not a>b:
    print("less")'''
'''a=5
b=9
if not a<b and b>a:
    print("less")'''
'''a=5
b=9
if not a<b or b>a:
    print("less")'''

'''a=int(input("enter a value"))
b=int(input("enter a value"))
if a<b and b>a:
    print("true")'''

'''a=int(input("enter a value"))
b=int(input("enter a value"))
if a!=b and b!=a:
    print("true")'''
#if-condition by using identify operators
#is,is not
'''a=7
if type(a)is int:
    print("it is not")'''

'''a=6
if type(a) is not int:
    print("false")'''

'''a=int(input("a value"))
if type(a) is int:
      print("true")'''
'''a=7.8
if type(a)is float:
    print("it is not")'''

'''a=7.8
if type(a)is not float:
    print("false")'''

'''a="bharani"
if type(a) is str:
    print(" true")'''

'''a="bharani"
if type(a) is not str:
    print(" true")'''

##if-condition by using membership operators
#in,not in
'''a=2,3,4,5,7,9,10
if 10 in a:
    print("true")'''


'''a=2,3,4,5,7,9,10
if 10 not in a:
    print("true") '''

'''a=2,3,4,5,7,9,10
if 20 not in a:
    print("true")'''

'''a=int(input("a value"))
if 30 in a:
    print("true")'''#error

'''a=[4,5,5,6,9,532,8,4]
b=int(input("value"))
if b in a:
    print("true")'''
        
#if-else conditions by using comparsion operators

'''a=6
b=3
if a<b:
    print("less")
else:
    print("true")'''


'''a=6
b=3
if a>b:
    print("less")
else:
    print("true")'''

'''a=6
b=3
if a<b:
    print("less")
else:
    a<=b
    print("true")'''

'''a=6
b=3
if a<b:
    print("less")
else:
    a!=b
    print("true")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a>b:
      print("true")
else:
    print("false")'''
#if-else statement by using logical operators
'''a=6
b=3
if a<b and b>a:
    print("less")
else:
    print("true")'''

'''a=6
b=3
if a<=b and b>=a:
    print("less")
else:
    print("true")'''

'''a=6
b=3
if a!=b and a==b:
    print("less")
else:
    print("true")'''

'''a=6
b=3
if a<b or b>a:
    print("less")
else:
    print("true")'''

'''a=6
b=3
if a<b not b>a:
    print("less")
else:
    print("true")'''
#if-elif conditions by using comparision
'''a=6
b=3
if a<b:  
    print("less")
elif b>a:
    print("greater")'''

'''a=6
b=3
if a==b:  
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("true")'''

'''a=2
b=4
if a==b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")'''

'''a=2
b=4
if a==b:
    print("less")
elif b<a:
    print("greater")
elif a!=b:
    print("not equal")'''
#if-elif-else
'''a=2
b=4
if a>b:
    print("greater")
elif a!=b:
    print("not equal")
elif a==b:
    print(" equal")
else:
    print("true")'''

'''a=2
b=4
if a<b:
    print("greater")
elif a!=b:
    print("not equal")
elif a==b:
    print(" equal")
else:
    print("true")'''
'''a=2
b=4
if a<b and b>a:
    print("greater")
elif a!=b or a==b:
    print("not equal")
else:
    print("true")'''

'''a=int(input(" a value"))
if type(a) is int:
    print("it is int")
else:
    print("non int")'''

'''a=int(input(" a value"))
if type(a) is int:
    print("it not  int")
else:
    print("non int")'''
        
#multiple-if
'''a=2
b=4
if a<b:
    print("greater")
if a!=b:
    print("not equal")
if a==b:
    print(" equal")'''

'''a=2
b=4
if b>a or a==b:
    print("greater")
if a<b:
    print("not equal")
if a!=b:
    print(" equal")'''

#nested-if

'''a=2
b=4
if a<b:
    print("less")
    if a!=b:
        print("greater")'''
'''a=2
b=3
if a==b:
    print("less")
    if b>a:
        print("greater")'''

'''a=15
b=20
if a<b:
    print("less")
    if b<a:
        print("greater")
    else:
        print("true")'''

'''a=15
b=20
if a<b:
    print("less")
    if b>a:
        print("greater")
    elif a!=b:
        print("not equal")'''

        




    


    

    


            


    


