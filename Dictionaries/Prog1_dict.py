record={}
n=int(input("Enter number of students:"))
i=1
while i<=n:
    name=input("Enter Student Name:")
    marks=input("Enter % of Marks of Student:")
    record[name]=marks
    i=i+1
print("Name of the Student","\t","% of Marks")
for x in record:
    print("\t",x,"\t\t",record[x])

