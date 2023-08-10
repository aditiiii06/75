sub1=int(input("enter marks of subject1: "))
sub2=int(input("enter marks of subject2: "))
sub3=int(input("enter marks of subject3: "))
sub4=int(input("enter marks of subject4: "))
sub5=int(input("enter marks of subject5: "))
total=sub1+sub2+sub3+sub4+sub5
print("total: ",total)
per=(total*100)/500
print("percentage: ",per)

if(per>=75) and (per<=100):
    print("result: distinction")
elif(per>=60) and (per<75):
    print("result:first class")
elif (per>=50) and (per<60):
    print("result: second class")
elif (per>=40) and (per<50):
    print("result: pass class")
else:
    print("result: fail")