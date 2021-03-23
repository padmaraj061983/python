class Employee:
    company_name="Mindmajix"
    def __init__(self):
        print("Constructor")
    
    def m1(self):
        self.y=900
        print("Method1")

e1=Employee()
e2=Employee()
print("e1",e1.company_name)
Employee.company_name="Mind"
e1.y=1000
print("e1",e1.company_name,e1.y)
e2.y=1100
print("e2",e2.company_name,e2.y)
