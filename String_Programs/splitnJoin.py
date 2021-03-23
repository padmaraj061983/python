s="Diabetic paitents are more in india"
l=s.split()
ll=[]
for x in l:
    ll.append(x)
print('list',ll)
#syntax join string = seperator.join(group of strings)
s=":".join(ll)
print("The String:",s)
