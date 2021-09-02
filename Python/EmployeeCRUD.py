import sys

class Employee:
    operation='Employee CRUD Operation'
    def __init__(self,name):
        self.name=name
        self.emplist=[]
    def add(self):
        emp=[]
        emp.append(int(input("ID: ")))
        emp.append(input("Name: "))
        emp.append(input("email: "))
        emp.append(float(input("Salary: ")))
        self.emplist.append(emp)
        print('Information Added')
        print(self.emplist)
    
    def delete(self):
        id=int(input("Enter ID to be Removed:"))
        self.emplist.pop(id)
        print(self.emplist)

    def print(self):
        print(self.emplist)

    def update(self,id):
        found=False
        for emp in self.emplist:
            if emp[0]==id:
                found=True
                print("ID Found")
                opt=int(input("Select the option you want to update \n1-Name \n2-email \n3-salary"))
                if opt == 1:
                    name=input("Input Updated Name: ")
                    emp[1]=name
                elif opt == 2:
                    email=input("Input Updated email: ")
                    emp[2]=email
                elif opt == 3:
                    salary=input("Input Update salary: ")
                    emp[3]=sal
            else:
                print("ID not Exist!")    

     
    
print('This is',Employee.operation)
name=input("Enter Name of User: ")
em=Employee(name)

while True:
    print('1-Add Employee \n2-Print Employee \n3-Delete Employee \n4-Update \n5-Exit')
    option=int(input("Select the Option"))
    if(option==1):
        em.add()
        
    elif(option==2):
        em.print()

    elif(option==3):
        em.delete()

    elif(option==4):
        id=int(input("Enter the ID to be Updated: "))
        em.update(id)

    elif(option==5):
        print('Thanks for Using this system')
        sys.exit()
    else:
        print('Invalid option..Plz choose valid option')

