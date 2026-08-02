#list comprehension
'''a=["python","dsa","java"]'''
#["python","dsa","java"]
#print(a.upper())error

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[expr for var in collection/range]
'''a=[i.upper() for i in a]
print(a)'''

'''a=["codegnan","course","python"]
#["Codegnan","Course","Python"]
b=[i.title() for i in a]
print(b)'''

'''a=[1,3,4,5,6,8,12,13]
b=[i*i for i in a]
b=[i**2 for i in a]
b=[pow(i,2) for i in a]
print(b)'''

#if-usage in list comprehension
#odd print no's
'''b=[i for i in range(21) if i%2!=0]
print(b)'''

#even print no's
'''b=[i for i in range(21) if i%2==0]
print(b)'''

#even no's squares
'''b=[i*i for i in range(21) if i%2==0]
print(b)'''

sD#odd no's squares
'''b=[i*i for i in range(21) if i%2!=0]
print(b)'''
#using membership
#in
'''a = ["apple", "banana", "mango", "dragon", "kiwi", "berry"]
b=[i for i in a if "a" in i]
print(b)'''

#not in

'''a = ["apple", "banana", "mango", "dragon", "kiwi", "berry"]
b=[i for i in a if "a" not in i]
print(b)'''

#no-elif usage in list comprehensions

#if-else usage in list comphrehensions
#range(16)
'''b=[i**2 if i%2==0 else i*5 for i in range(16)]
print(b)'''

#a=[1,2,3,4,5]
#b=[5,4,3,2,1]

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]'''
#[6,6,6,6,6]
'''c=[a[i]+b[i] for i in range(len(a))]
print(c)'''

'''c=[a[i]+b[i] for i in range(5)]
print(c)'''
















