#               القوائم المتداخلة
#               nested lists

# name=[ ["Apples" , "Bananas"] ,["Milk" , "Water"] ]
# num=[ "Cake" , "Candy"]
# num.insert(0,"Coffe")
# name.insert([0][0],"Btaths")
# name.append(num)
# print(name)

# print(name[0][0],name[1][0])
# #*************************************************
print([ ["Apples" , "Bananas"] ,["Milk" , "Water"]])
nam=[1, 2, 3]
name=["Apples" , "Bananas"]
nump=["Milk" , "Water"]
num=input("Press enter to change the content .....")
if num:
    print("No , Sorry")
else:
    print("Here is the updated basket")
    
    
    name.insert(0,"Oranges")
    name.insert(3,"Kiwis")
    nump.insert(0,"Coffee")
    nump.append("Tea")
    nump.remove('Water')
    name.append(nump)
    name.append(nam)
    print(name)
    # name.append(nam)
    # print(name)
    
    
#||****************البرنامج بصيغة مختلفة *****************||


opp=[["Apples", "Bananas"], ["Milk", "Water"]]
print(opp)
nump=input("Press neter to change the content.........")

if nump:
    
    print("Sorre, No")
else:
    
    print("Here is the updated basket")
    opp[1].remove('Water')
    
    opp[0].insert(0,"Oranges")
    opp[0].insert(3,"Kiwis")
    opp[1].insert(0,"Coffee")
    
    opp[1].insert(2,"Tea")
    opp.append([1, 2, 3])
    
    
    print(opp)
        
