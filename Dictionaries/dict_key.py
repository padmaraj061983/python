d={100: 'Padma', 200: 'Raj', 300: 'pavani', 400: 'dev'}
print("*"*20,"Keys Example","*"*20)
print(d.keys())
for k in d.keys():
    print(k)
print("*"*20,"Values Example","*"*20)
print(d.values())
for val in d.values():
    print(val)
print("*"*20,"Items Example","*"*20)
for k,v in d.items():
    print(k,"__",v)
