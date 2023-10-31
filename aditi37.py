import datetime
from itertools import permutations
now=datetime.datetime.now()
class Busbooking:
	def __init__(self,name__l,age__l,sex__l,from_l,to_l) :
		self.name__l=name__l
		self.age__l=age__l
		self.sex__l=sex__l
		self.from_l=from_l
		self.to_l=to_l
class ticket:
	def __init__(self,lst):
		self.lst=lst
	@classmethod
	def sol(cls,lst):
		print("\n\nTicket Booking System\n")
		restart = ('Y')
		while restart != ('N','NO','n','no'):
			print("1.Check PNR status")
			print("2.Ticket Reservation")
			option = int(input("\nEnter your option : "))

			if option == 1:
				print("Your PNR status is t3")
				exit(0)

			elif option == 2:
				people = int(input("\nEnter no. of Ticket you want : "))
				name_l = []
				age_l =[]
				sex_l = []
				from_l=[]
				from2=["kolhapur","sangli","pune","satara","nashik","mumbai","nagpur"]
				perm=permutations(["kolhapur","sangli","pune","satara","nashik","mumbai","nagpur"],2)
				to_l=[]
				to1=["kolhapur","sangli","pune","satara","nashik","mumbai","nagpur"]
				for p in range(people):
					price=0
					name = str(input("\nName : "))
					name_l.append(name)
					age  = int(input("\nAge  : "))
					age_l.append(age)
					sex  = str(input("\nMale or Female : "))
					sex_l.append(sex)
					from1=str(input("from[""(kolhapur)""(sangli)""(pune)""(satara)""(nashik)""(mumbai)""(nagpur):"))
					if from1 in from2:
						from_l.append(from1)
					to=str(input("to[""(kolhapur)""(sangli)""(pune)""(satara)""(nashik)""(mumbai)""(nagpur):"))
					if to in to1:
						to_l.append(to)
					if from1==to:
						price+=0
					elif(from1=="kolhapur" and to=="nagpur"):
						price+=500
					elif(from1=="sangli" and to=="kolhapur"):
						price+=100
					elif(from1=="pune" and to=="kolhapur"):
						price+=300
					elif(from1=="pune" and to=="nagpur"):
						price+=400
					elif(from1=="kolhapur" and to=="satara"):
						price+=200
					elif(from1=="kolhapur" and to=="nashik"):
						price+=150
					elif(from1=="kolhapur" and to=="sangli"):
						price+=50
					elif(from1=="kolhapur" and to=="pune"):
						price+=300
					elif(from1=="kolhapur" and to=="mumbai"):
						price+=500
				restart = str(input("\nDid you forgot someone? y/n: "))
				if restart in ('y','YES','yes','Yes'):
					restart = ('Y')
				else :
					x = 0
					print("\nTotal Ticket : ",people)
					for p in range(1,people+1):
						for k in range(25):
							print("-",end=" ")
							if k==30:
								break
						print("-")
						print("|****BUS BOOKING****")
						print("|Ticket : ",p)
						print("|Name : ", name_l)
						print("|Age  : ", age_l)
						print("|Sex : ",sex_l)
						print("|from : ",from_l)
						print("|to: ",to_l)
						print("|price: ",price)
						print(now.strftime("|%Y-%m-%d %H:%M"))
						for z in range(25):
							print("-",end=" ")
						print("_")
						x += 1
lst=input("ENTER SOMETHING TO START")
ticket.sol(lst)
# ('kolhapur', 'sangli')
# ('kolhapur', 'pune')
# ('kolhapur', 'satara')
# ('kolhapur', 'nashik')
# ('kolhapur', 'mumbai')
# ('kolhapur', 'nagpur')
# ('sangli', 'kolhapur')
# ('sangli', 'pune')
# ('sangli', 'satara')
# ('sangli', 'nashik')
# ('sangli', 'mumbai')
# ('sangli', 'nagpur')
# ('pune', 'kolhapur')
# ('pune', 'sangli')
# ('pune', 'satara')
# ('pune', 'nashik')
# ('pune', 'mumbai')
# ('pune', 'nagpur')
# ('satara', 'kolhapur')
# ('satara', 'sangli')
# ('satara', 'pune')
# ('satara', 'nashik')
# ('satara', 'mumbai')
# ('satara', 'nagpur')
# ('nashik', 'kolhapur')
# ('nashik', 'sangli')
# ('nashik', 'pune')
# ('nashik', 'satara')
# ('nashik', 'mumbai')
# ('nashik', 'nagpur')
# ('mumbai', 'kolhapur')
# ('mumbai', 'sangli')
# ('mumbai', 'pune')
# ('mumbai', 'satara')
# ('mumbai', 'nashik')
# ('mumbai', 'nagpur')
# ('nagpur', 'kolhapur')
# ('nagpur', 'sangli')
# ('nagpur', 'pune')
# ('nagpur', 'satara')
# ('nagpur', 'nashik')
# ('nagpur', 'mumbai')