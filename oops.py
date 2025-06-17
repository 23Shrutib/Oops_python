'''
#Student Example:->
class Student:  #class

    def info(self): #self contains object memory(s1)  #function/method
        self.roll=int(input("Enter Roll "))  #s1.roll
        self.name=input("Enter Name ")  #s1.name
        self.marks=float(input("Enter marks ")) #s1.marks

    def display(self):  #function/method
        print(f'Roll:{self.roll} Name:{self.name} Marks:{self.marks}')

s1=Student() #s1 is object
s1.info()
s1.display()
'''


'''
#Employee Example:->
class Employee:
    def info(self): #self contain object e1
        self.eid=int(input("Enter ID "))
        self.name=input("Enter name ")
        self.salary=float(input("Enter Salary "))
    
    def display(self):
        print(f'ID:{self.eid} Name:{self.name} Salary:{self.salary}')

e1=Employee()
e1.info()
e1.display()
'''

############16june #CONSTRUCTOR
'''
class Employee: #class
    def __init__(self): #constructor
        self.eid=int(input("Enter ID "))
        self.name=input("Enter Name ")
        self.salary=float(input("enter Salary "))

    def display(self): #method- (instance method)
        print(f'ID:{self.eid} Name:{self.name} Salary:{self.salary}')


e1=Employee() #e1 is object
#constructor gets automatically called at the time of creation.
e1.display()
'''

'''
#constructor student example##############
class Student:  #class

    def __init__(self): #constructor
        self.roll=int(input("Enter Roll "))  
        self.name=input("Enter Name ") 
        self.marks=float(input("Enter marks "))

    def display(self): #method- (instance method)
        print(f'Roll:{self.roll} Name:{self.name} Marks:{self.marks}')

s1=Student() #s1 is object
s1.display()
'''


'''
#Parameterised Constructor
class Employee: #class
    def __init__(self,eid,name,salary): #parameterised constructor
        self.eid=eid
        self.name=name
        self.salary=salary

    def display(self): #method- (instance method)
        print(f'ID:{self.eid} Name:{self.name} Salary:{self.salary}')


e1=Employee(1,"shruti",8475.56) #e1 is object
#constructor gets automatically called at the time of object creation.

e2=Employee(2,"tanu",5644.11)   #you can call multiple times ex. e1,e2,e3

e1.display()
e2.display()
'''


'''
#parameterised constructor student example:-
class Student:  #class

    def __init__(self,roll,name,marks): #parameterised constructor
        self.roll=roll  
        self.name=name
        self.marks=marks

    def display(self): #method- (instance method)
        print(f'Roll:{self.roll} Name:{self.name} Marks:{self.marks}')

s1=Student(101,"tannu",88.5) #s1 is object
s1.display()
'''



'''
#Using data structure:-----
class Employee: #class
    def __init__(self): #constructor
        self.eid=int(input("Enter ID "))
        self.name=input("Enter Name ")
        self.salary=float(input("Enter Salary "))

    def display(self): #method- (instance method)
        print(f'ID:{self.eid} Name:{self.name} Salary:{self.salary}')

data=[]  #[e1,e1,e1]
n=int(input("Enter number "))  #ex. 3
for i in range(n):
    e1=Employee() 
    data.append(e1)
    
for i in data:
    i.display() #e1.display
'''


'''
########STUDENT EXAMPLE:-
class Student:  #class

    def __init__(self): #constructor
        self.roll=int(input("Enter Roll "))  
        self.name=input("Enter Name ") 
        self.marks=float(input("Enter marks "))

    def display(self): #method- (instance method)
        print(f'Roll:{self.roll} Name:{self.name} Marks:{self.marks}')

data=[]
n=int(input("Enter number "))
for i in range(n):
    s1=Student() #s1 is obj
    data.append(s1)

for i in data:
    i.display() #e1.display
'''






