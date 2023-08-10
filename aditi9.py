a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
c=int(input("enter value of c: "))

if(a<b and a>c):
    print("a is largest")
elif(b>a and b>c):
    print("b is largest")
elif(c>a and c>b):
    print("c is largest")
elif(a==b and a>c):
    print("a and b is equal and is largest then c")
elif(a==b and a>b):
    print("a and b is equal and is largest then b")
elif (c==b and c>a):
    print("b and c are equal and is largest then a")
else:
    print("all are equal")