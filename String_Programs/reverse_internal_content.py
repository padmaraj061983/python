# Mindmajix Is Learning School
# xijamdniM sI gninraeL loohcS

s=input("Enter a line:")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=' '.join(l1)
print(output)
