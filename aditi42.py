""""usd=float(input("Enter currency in USD: "))
inr=usd*73
print("The currency in INP:",round(inr,2))"""

""""mb1=0.00000125
gb1=0.00000000125
tb1=0.00000000000125
b=int(input("Enter bits:"))
mb=b*mb1
gb=b*gb1
tb=b*tb1
print(b,"Bits=",mb,"Megabytes")
print(b,"Bits=",gb,"Gigabytes")
print(b,"Bite=",tb,"Terabytes")"""

""""num=int(input("Enter number to find square root"))
print("The square root of number is:",(num*num))"""



""""l=float(input("Enter a length:"))
b=float(input("Enter a breath:"))
area=l*b
print(area)"""

""""s=int(input("Enter side:"))
area=s*s
permimeter=4*s
print("area",area)
print("Permimeter",permimeter)"""


"""a=int(input("Enter a number a:"))
b=int(input("Enter a number b:"))
var=a
a=b
b=var
print("Number after swapping",a)
print("Number after swapping",b)
"""

""""print("Even numbers from 1 to 100")
i=0
while i<=100:
    if (i%2==0):
        print(i)
    i=i+1"""

"""sum=0
for i in range(0,11):
    sum=sum+i
print(sum)"""

#fibonicci
""""n=int(input("Enter limit for fibonicci:"))
a=0
b=i=1
print(a)
print(b)
while i<=n:
    c=a+b
    print(c)
    a=b
    b=c
    c=a
    i=i+1"""

""""n=int(input("Enter number for factorial:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)"""


"""n=int(input("Enter a number to reverse"))
rem=0
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("Reverse of number is")
print(rev)"""

""""n=int(input("Enter a number" ))
total=0
while (n>0):
     digit=n%10
     total=total+digit
     n=n//10
print(total)"""


"""n=int(input("Enter a number:"))
rem=0
rev=0
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(temp==rev):
    print("palidrome")
else:
    print("Not palidromme")"""


"""sum=0
list1=[1,2,3,4,5,6,7,8,9]
for i in list1:
    sum=sum+i
print("Sum of all elements in list",sum)"""

""""list=[123,432,435,667]
print(max(list))"""

"""list1=["feg",123,4.5,"xyz"]
list1.reverse()
print(list1)"""


""""list1=[1,2,3,4,5,6,57]
list2=[7,8,9,57.,78,45]
for i in list1:
    for j in list2:
        if(i==j):
            print(i,"is common")"""

""""tup=(123,5647,5673,3947,27327)
print(max(tup))
print(min(tup))"""

""""tup1=(1,2,3,4,5,6,7,9,7,4)
repeat=[]
for i in tup1:
    if tup1.count(i)>1:
        repeat.append(i)
for x in repeat:
    if repeat.count(x)>1:
        repeat.remove(x)
print("repeated items: ",repeat)"""


""""tup1=("zero","one","two","three","four","Five","six","Seven","eoght","nine")
num=input("Enter number")
word=[]
for i in num:
    word.append(tup1[int(i)])
    print(word)"""

""""set1={1,2,3,4,5}
set1.add(8)
print(set1)
set1.remove(5)
print(set1)"""

""""set1={1,2,3,4,5,6,7,8}
set2={3,7,9,0,34,56,44}
print("Union of sets :",set1|set2)
print("interection of sets", set1 & set2)
print("Set difference",set1-set2)"""


""""dict={5:1,7:6,6:7,3:4,8:9}
print("original dictinary",dict)
sort=sorted(dict.values())
print("Ascending order",sort)
sort=sorted(dict.values(),reverse=True)
print(sort)"""

""""di1={"a":3,"b":5,"c":4}
di2={"d":7,"e":2,"f":9}
di3={}
for d in di1,di2:
    di3.update(d)
    print(di3)"""

""""d1={'a':100,'b':200,'c':400}
d2={'a':300,'b':200,'d':400}
d3={}
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            d3[i]=(j+y)
print(d3)
"""


""""from collections import Counter
dict1={"Ä":3754,"B":3743,"C":3652,"D":9807,"E":2762}
print(dict1)
k=Counter(dict1)
highest=k.most_common(3)
for i in highest:
    print(i[0],":",i[1],)"""


"""
#practical 16
"""

"""
#program to check for zero division Error exception
x=int(input("Enter first value:"))
y=int(input("Enter second value:"))
try:
    result=x/y
except ZeroDivisionError:
    print("Division by Zero")
else:
    print("Result is:",result)
finally:
    print("Execute finally clause")
    
"""


"""
#program to create user defined exception
#that will check whether the password is correct or not
class error(Exception):
    pass
class wrongpassword(error):
    pass
while True:
    try:
        password=input("Enter Password:")
        if(password!='computer'):
            raise wrongpassword
        else:
            print("password is correct")
            break
    except wrongpassword:
            print("Wrong Password\n")
            
"""

"""
#create a class employee with data members :name,department and slary.create suitable methods for reading and printing suitable information
class employee:
    name=""
    department=""
    salary= 0
    def get(self):
        self.name=input("Enter Name: ")
        self.department=input("Enter Department: ")
        self.salary=input("Enter Salary: ")
    def put(self):
        print("Employee Name: ",self.name)
        print("Employee Department: ",self.department)
        print("Employee Salary: ",self.salary)
e=employee()
print("Enter Details")
e.get()
print("\n\n Displaying Details")
e.put()
"""

"""
#python program to read an print students information usig two classes using simple inheritance
class student:
    def _init_(self,name,roll):
        self.name=name
        self.roll=roll
class stud(student):
    def _init_(self,name,roll):
        student._init_(self,name,roll)
    def print_details(self):
        print("Name: ",self.name)
        print("Roll No: ",self.roll)
name=input("Enter Student Name: ")
roll=int(input("Enter Roll No: "))
s1=stud(name,roll)
s1.print_details()
"""

"""
#write a program to implement multiple inheritance
class person:
    def accept_personal_details(self):
        self.name=input("Enter Person Name: ")
        self.contact=int(input("Enter contact number: "))
        self.dob=input("Enter DOB: ")
    def show_personal_details(self):
        print("Person Name: ",self.name)
        print("Contact number: ",self.contact)
        print("DOB:",self.dob)
class bankaccount:
    def accept_bank_details(self):
        self.accno=int(input("Enter Account Number: "))
        self.acctype=input("Enter Account Type: ")
        self.ifsc=input("Enter IFSC code: ")
    def show_bank_details(self):
        print("Account Number: ",self.accno)
        print("Account Type: ",self.acctype)
        print("IFSC code: ",self.ifsc)

class gasconnection(person, bankaccount):
    def accept_consumer_details(self):
        self.consumer_num=int(input("Enter Consumer Number: "))
        self.no_cy=int(input("Enter Number of Cylinders: "))
        self.deposit=int(input("Enter Deposit Amount: "))

    def show_consumer_details(self):
        print("Consumer Number: ",self.consumer_num)
        print("Number of Cylinders: ",self.no_cy)
        print("Deposit Amount: ",self.deposit)
obj1=gasconnection()
obj2=gasconnection()
print("Accepting Details of Customer 1")
obj1.accept_personal_details()
obj1.accept_bank_details()
obj1.accept_consumer_details()
print("Accepting Details of Customer 2")
obj2.accept_personal_details()
obj2.accept_bank_details()
obj2.accept_consumer_details()
print("Showing Details of Customer 1")
obj1.show_personal_details()
obj1.show_bank_details()
obj1.show_consumer_details()
print("Showing Details of Customer 2")
obj2.show_personal_details()
obj2.show_bank_details()
obj2.show_consumer_details()
"""

"""
#Program to create a class to print an integer and a character with two mwthods having the samename but different sequence of integer and the charcter parameters
class example:
    def disp(self,a,b):
        print(a)
        print(b)
obj=example()
obj.disp(10,"A")
obj.disp("B",20)
"""
""""
#program to create a class to print the area of square and a rectangle
class area:
    def area(self,a,b=none):
        if b==none:
            return a*a
        else:
            return a*b
a1=area()
print("Area of square:",a1.area(10))
print("Area of rectangle:",a1.area(5,6))
"""
""""
# write a pyhton program to create a class 'Degree' having  a method 'getDegree' that prints "I got a degree".
class degree():
    def getdegree(s):
        print("I got a degree")
class undergraduate(degree):
    def getdegree(s):
        print("I am undergraduate")
class postgraduate(degree):
    def getdegree(s):
        print("I am Postgraduate")
c1=postgraduate()
c1.getdegree()
c1=undergraduate()
c1.getdegree()
c1=degree()
c1.getdegree()
"""

#composition:
class gmail:
    def send_email(self,msg):
        print("Sending '{}' from gamil".format(msg))
class yahoo:
    def send_email(self,msg):
        print("Sending '{}' from yahoo".format(msg))
class email:
    provider=gmail()
    def set_provider(self,provider):
        self.provider=provider
    def send_email(self,msg):
        self.provider.send_email(msg)
client1 =email()
client1.send_email("Hello")
client1.set_provider(yahoo())
client1.send_email("Hello")
    






