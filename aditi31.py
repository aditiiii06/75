n=int(input("Enter a Number: ")) 
rem=0 
rev=0 
temp=n 
while n>0: 
    rem=n%10 
    rev=rev*10+rem 
    n=n//10 
if(temp==rev): 
    print("Entered number is ",temp,"Reverse of number is ",rev) 
    print("Number is Palindrome") 
else: 
    print("Entered number is ",temp,"Reverse of number is ",rev) 
    print("Number is not Palindrome")

