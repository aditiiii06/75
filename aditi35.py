str="Bus Booking"
str2=str.center(40)
name=input("Enter your name:")[:6]
age=int(input("Enter your age:"))
address=input("Enter your address:")[:9]
sex=input("Enter your sex:")[:4]
phone=int(input("Enter your phone number:"))
from1=input("Enter the location from where you want to start journey:")[:8]
to=input("Enter the location you want to go:")[:8]
date2=input("Enter the date of journey")
price=500
time2=input("enter time to start")


for k in range(25):
    print("-",end=" ")
    if k==30:
        break
print("-")
print(f"|   {str2}   |")
print(f"|Name={name}",end="                ")
print(f"Age={age}              |")
print(f"|Address={address}",end="          ")
print(f"M/F={sex}            |")
print(f"|Phone={phone}                              |")
print(f"|To={to}",end="                 ")
print(f"From={from1}       |")
print(f"|Date={date2}                               |")
print(f"|Time={time2}                                      |")
print(f"|Price={price}                                      |")
for z in range(25):
    print("-",end=" ")




