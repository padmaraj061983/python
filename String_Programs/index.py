s=input("Enter main String")
subs=input("Enter sub String:")
try:
    n=s.index(subs)
except ValueError:
    print("Substring is not found")
else: 
    print("Substring Found")
