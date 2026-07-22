#print no's 1to 10
'''i=1
while i<=10:
    print(i)
    i=i+1'''
#print 10 to 1
'''i=10
while i>=1:
    print(i)
    i=i-1'''\
#print even 1 to 2 
'''i=2
while i<=20:
    print(i)
    i=i+2'''

# ATM Application

account = 100000
card = "c"
pwd = 1234

insert_card = input("Insert Card (c): ")

if insert_card == card:
    password = int(input("Enter Password: "))

    if password == pwd:
        print("Password Correct")
        print("----- ATM MENU -----")
        print("1. Balance Enquiry")
        print("2. Withdraw")

        option = int(input("Enter Option: "))

        if option == 1:
            print("Account Balance =", account)

        elif option == 2:
            amount = int(input("Enter Withdraw Amount: "))

            if amount <= account:
                account = account - amount
                print("Please Collect Your Cash")
                print("Remaining Balance =", account)
            else:
                print("Insufficient Balance")

        else:
            print("Invalid Option")

    else:
        print("Incorrect Password")

else:
    print("Invalid Card")
