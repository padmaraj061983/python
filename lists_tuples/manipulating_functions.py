list1=[]
list1.append("A")
list1.append("B")
list1.append("C")
print(list1)
n=[1,2,3,4,5]
n.insert(1,777)
print(n)
list1.extend(n)
print("Extending List:",list1)
n.remove(1)
print("list n:",n)
