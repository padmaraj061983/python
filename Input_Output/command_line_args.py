import sys
n=len(sys.argv)  # n is the number of arguments 3
args= sys.argv   # args list contains arguments inp1 inp2 inp3 
print('No of Command line args:',n)
print('The args are:', args)

for a in args:
    print(a)
