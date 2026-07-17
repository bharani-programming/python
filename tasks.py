#taskes
'''a=[9,7,4,0,1,5,10,8,6,3]
a.sort()
print(a)'''

'''a=("apple","banana","mango")
b=list(a)
b.append("grapes")
print(b)

c=tuple(a)
print(c)
print(type(c))'''

'''a="idno:234155S\nname:bharani\nmailid:nandambharani@gmail.com\nmobileno:9381042690\ncollege:s.d.m.s.m.k\nbranch:computer science"
print(a)'''

'''idno=int(input("enter the id"))
name=input("enter the name")
mobileno=int(input("enter the mobile no"))
mailid=input("enter the mailid")
college=input("enter the college name")
branch=input("enter the branch")
print(".....................STUDENT PROFILE..........................")
print("id no is",idno)
print("name is",name)
print("mobileno is",mobileno)
print("mailid is",mailid)
print("college is",college)
print("branch is ",branch)'''
     #RUN TIME TASKES
#voting
age=int(input("enter value"))
if age>=18:
    print("eligible for vote")
else:
        print("not eligible")
#even or odd
num=int(input("enter a value"))
if num%2==0:
    print("even")
else:
    print("odd")
#leap year
year=int(input("enter a value"))
if year%4==0:
         print("leap year")
else:      print("not a leap year")

a=input()
if a=="bharani":
      print("welcome",a)
else:
    print("welcome guest")
    
a=input().upper()
if a=="bharani":
      print("WELCOME",a)
else:
    print("WELCOME GUEST")

a=["devi","bharani","teja","pushpa","chinni"]
b=input().lower()
if b in a:
      print("welcome",b)
else:
    print("welcome guest")

#vowels &consonat

Letter=["a","e","i","o","u"]
a=input("letter").lower()
if a in letter:
    print("it is  vowel")
else:
    print("it is consonat")



