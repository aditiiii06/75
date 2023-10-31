import datetime
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
					from1=str(input("from where you wish to start journey""(kolhapur)""(sangli)""(pune)""(satara)""(nashik)""(mumbai)""(nagpur)"))
					if from1 in from2:
						from_l.append(from1)
					to=str(input("to which place you wish to visit""(kolhapur)""(sangli)""(pune)""(satara)""(nashik)""(mumbai)""(nagpur)"))
					if to in to1:
						to_l.append(to)
					if from1==to:
						price+=0
					elif(from1=="kolhapur" and to=="nagpur"):
						price+=500
					elif(from1=="sangli" and to=="kolhapur"):