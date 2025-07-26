
name=input("Enter Your is names type is comme: ").split(", ")

paser=[]

for num in name:
    numbr=num.split()
    print(numbr)
    
    opp=numbr[0]
    oop=numbr[1]
    on=opp[0]
    to=oop[0]
    
    sume=on+"."+to+"."
    paser.append(sume)
    
print("الاختصارات:")
for x in paser:
    print(x)     
    
    
