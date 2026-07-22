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
'''while True:
    age=int(input("enter value"))
    if age>=18:
        print("eligible for vote")
    else:
            print("not eligible")'''
#even or odd
'''num=int(input("enter a value"))
if num%2==0:
    print("even")
else:
    print("odd")'''
#leap year
'''year=int(input("enter a value"))
if year%4==0:
         print("leap year")
else:      print("not a leap year")'''

'''a=input()
if a=="bharani":
      print("welcome",a)
else:
    print("welcome guest")'''
    
'''a=input().upper()
if a=="bharani":
      print("WELCOME",a)
else:
    print("WELCOME GUEST")'''

'''a=["devi","bharani","teja","pushpa","chinni"]
b=input().lower()
if b in a:
      print("welcome",b)
else:
    print("welcome guest")'''

#vowels &consonat

'''Letter=["a","e","i","o","u"]
a=input("letter").lower()
if a in letter:
    print("it is  vowel")
else:
    print("it is consonat")'''

# Social Media Login using Nested if

'''name = input("Enter your name: ")
password = input("Enter your password: ")
if name == "bharani":
    if password == "12345":
        print("Login Successful")
else:
        print("invalid credentials")'''

'''username = input("Enter your username: ")
password = int(input("Enter your password: "))
if username == "bharani":
    if password == 12345:
        print("Login Successful")
else:
        print("invalid credentials")'''

'''username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "bharani" and password == "bharani@12345":
        print("Login Successful")
else:
        print("invalid credentials")'''

'''age=int(input("enter a age"))
marks=int(input("enter a marks"))
attendance=int(input("enter a number"))
if age>=18:
         print("eligible for vote")
if marks>=70:
         print("allow to write exams")
if attendance>=80:
         print("they are eligible for scholarship")'''

'''age=int(input("enter a age"))
marks=int(input("enter a marks"))
attendance=int(input("enter a number"))
if age>=18:
         print("eligible for vote")
else:
    print("not eligible for vote")
if marks>=70:
         print("allow to write exams")
else:
    print("not allow to write a exams")
if attendance>=80:
    print("they are eligible for scholarship")
else:
    print("not eligible for scholarship")'''

#if-elif-else
'''cake=input("choose a cake name")
if cake=="red velvet":
    print("cost is 1200 rupees")
elif cake=="choco almond":
    print("cost is 1000 rupees")
elif cake=="honey almond":
    print("cost is 800 rupees")
elif cake=="butter scotch":
    print("cost is 600 rupees")
else:
    print("cake is not avaiable")'''

'''cake=input("choose a cake name")
if cake=="red velvet":
    print(1200)
elif cake=="choco almond":
    print(1000)
elif cake=="honey almond":
    print(800)
elif cake=="butter scotch":
    print(600)
else:
    print("cake is not avaiable")'''

'''price=int(input("choose price"))
if price==1000:
    print("BBQ pizza")
elif price==800:
    print("crispy chicken pizza")
elif price==600:
    print("paneer pizza")
elif price==400:
    print("corn pizza")
elif price==200:
    print("french frics&coke")'''

###students grades
'''while True:
        student = int(input("Enter marks: "))
        if student in range(91, 101):
            print("Grade-A")
        elif student in range(81, 91):
            print("Grade-B")
        elif student in range(71, 81):
            print("Grade-C")
        elif student in range(50, 71):
            print("Grade-D")
        else:
            print("Fail,study well.......")'''


'''student = int(input("Enter marks: "))
for student in range(91, 101):
    print("Grade-A")'''
#ATM APPLICATION
while True:
    account=100000
    card="c"
    pwd=93810
    insert_card=input("insert card(c):").lower()
    if insert_card==card:
        print("welcome bharani")
        password=int(input("enter a password"))
        if password==pwd:
               print("password correct")
               print("------ATM MEMU------")
               print("1.balance enquriy")
               print("2.withdraw")
               option=int(input("enter option: ")) 
               if option==1:
                  print("Account Balance=",account)
               elif option==2:
                    amount=int(input("enter a withdraw amount"))
                    print(amount)
                    account=account-amount
                    print("enter the cash")
                    print("remaning balance=",account)
               else:
                   print("inavlid option")
        else:
            print("incorrect password")
            
    else:
        print("invalid card")

     
            
        
        


                   





