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
'''#ATM APPLICATION
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
        print("invalid card")'''
#attendance report
'''n=int(input("enter the total no.of student"))
countp=0
counta=0
for i in range(1,n+1):
   s=input("student {} present or absent:".format(i)).lower()
   if s=="p":
       countp=countp+1
   elif s=="a":
       counta=counta+1
print("................ATTENDENCE REPORTS...............")
print("total student",n)
print("total presenties",countp)
print("total absenties",counta)'''

#BMI calculator
'''while True:
   w=float(input("enter a weight"))
   h=float(input("enter a height"))
   c=w/(h)**2        
   if c<=18.5:
      print("under weight")
   elif c>18.5 and c<=24.5:
      print("healthy weight")
   elif c>24.5 and c<=29.5:
      print("over weight")
   elif c>30:
      print("obesity")'''
#patterns
#right angle
'''n=6
for i in range(1,n+1):
   print(" * "*i)'''
#reversed angle
'''n=5
for i in range(n,0,-1):
   print(" * "*i)'''

'''n=6
for i in range(n):
   print("*"*(n-i))'''
'''n=5
#square
for i in range(n):
   for j in range(n):
      print(" * ",end="")
   print()'''

'''n=4
for i in range(1,n+1):
   print(" "*(n-i)+" * "*i)'''

def split_bill():
    amount = int(input("Enter total bill amount: "))
    persons = int(input("Enter number of persons: "))

    if persons > 0:
        each = amount / persons
        print("Each person should pay:", each)
    else:
        print("Number of persons must be greater than 0")

split_bill()
            
'''def split_bill():
    amount = int(input("Enter bill amount: "))
    persons = int(input("Enter number of persons: "))

    if persons <= 0:
        print("Invalid number of persons")
    else:
        print("Each person pays:", amount / persons)

def exit_program():
    print("Thank You!")

while True:
    print("\n1. Split Bill")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        split_bill()
    elif choice == 2:
        exit_program()
        break
    else:
        print("Invalid Choice")'''
'''#normal
def split_bill():
   a=int(input("enter how many people"))
   b=int(input("enter a amount"))
   print("per head bill",b//a)
split_bill '''
'''#format
def split_bill():
    a=int(input("enter how many people"))
    b=int(input("enter a amount"))
    print(f"per head bill{b//a}")
    print("per head bill{}".format(b//a))
split_bill'''
#fstrings
'''def split_bill():
    a=int(input("enter how many people"))
    b=int(input("enter a amount"))
    c=b/a
    print(f"per head bill{c}")
    print("per head bill{}".format(c))
split_bill'''
   
'''num = int(input("Enter a number (1-100): "))

values = [100, 90, 50, 40, 10, 9, 5, 4, 1,]
symbols = ["C", "XC", "L", "XL", "X", "IX", "V", "IV", "I",]

roman = ""

for i in range(len(values)):
    while num >= values[i]:
        roman += symbols[i]
        num -= values[i]

print("Roman Numeral:", roman)'''

'''roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

for i in range(10):
    print(i + 1, "=", roman[i])'''

#railway ticket
'''print("............. Railway Ticket .............")

ticket=1000
gender=input("Choose gender (male/female): ").lower()

def male():
    age=int(input("Enter Age: "))
    if age > 60:
        fare=ticket - (ticket * 30 / 100)
    else:
        fare=ticket
    print("Ticket Fare =", fare)

def female():
    age=int(input("Enter Age: "))
    if age > 60:
        fare=ticket - (ticket * 50 / 100)
    else:
        fare=ticket - (ticket * 30 / 100)
    print("Ticket Fare =", fare)

if gender=="male":
    male()
elif gender=="female":
    female()'''  
   

        






       
    
    
            
        
        


                   





