def fact(num):
    result=1
    while num >=1:
        result=result*num
        num=num-1
    return result

for i in range(1,5):
    print("The factorial of",i,"is:",fact(i))

# Recursive means the function calling itself

def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1) # 4*factorial**factorial(2)*factorial(1)=3*2*1
    return result
print("factorial of 3",factorial(3))
print("factorial of 4",factorial(4))
