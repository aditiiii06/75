""""class vehicle:
    name="Maruti"
    def display(self):
        print("Name =",self.name)
class category(vehicle):
    price="400000"
    def disp_price(self):
        print("price",self.price)
car1=category()
car1.display()
car1.disp_price()"""

class employee:
    def __init__(self,name,age,dep,sal):
        self.name=input("Enter name of employee")
        self.age=input("Enter age of employee")
        self.dept=input("Enter department ")
        self.sal=input("Enter salaray")
    def emp(self):
        print("NAme of employee",self.name)
        print("Age of employee",self.age)
        #print("Name of"+self.name+,+self.sal)
        print("Salary of "+self.name+ "is",+self.sal)
    def emp1(self):
        print("NAme of employee",self.name)
        print("Age of employee",self.age)
        #print("Name of"+self.name+"is", +self.sal)
        print("Salary of"+self.name+"is",+self.sal)
empc=employee("","",0)
empc1=employee("","",0)
empc.emp()
empc1.emp1()

        