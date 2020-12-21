s={10,20,30,40,50}
s.add(70)
print("After s.add(70)",s)
l=[60,80,90,100]
s.update(l)
print("After the s.update",s)
s1=s.copy()
print("Set1 set",s1)
print("Popped list",s1.pop())
s1.remove(50)
print("After removing 50",s1)
s1.discard(50)
x={10,20,30,40}
y={30,40,50,60}
print("Union Operation",x.union(y))
print("Intersection Operation",x.intersection(y))
print("Difference Operation",x.difference(y))

