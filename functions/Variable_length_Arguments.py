def sum(*n): # Variable length arguments
    total=0
    for n1 in n:
        total=total+n1
    print("The sum is:",total)

sum()
sum(10)
sum(10,20)
sum(10,20,30,40)
sum(10,20,30,40,50,60,70)
