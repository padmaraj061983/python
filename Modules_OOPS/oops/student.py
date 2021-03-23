class Student:
    """ The is student class"""
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def talk(self):
        print("Hello My name is:",self.name)
        print("My Rollno is:",self.rollno)
        print("My Marks are:",self.marks)
s1=Student("Padma",101,80)
print(s1.__dict__)
print(s1.name,s1.marks)
s1.talk()
