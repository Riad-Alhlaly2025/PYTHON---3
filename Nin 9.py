


#***************** برنامج يطلب منك ادخال اسماء ويسالك على كل اسم ********
# name=input("Enter is the names commas: ").split(", ")

# num=[]
# nuu=[]
# for entr in name:
#     print(f"\n {entr} \n")
#     opp=input(f"Your have numbrkt {entr} (Yes or No): ").lower()
#     if opp =='yes':
#         print(f"\n Good fride")
#         num.append(entr)
#     else:
#         print("\n Sorre, Agine")
#         nuu.append(entr)
#     print("----------------")
  
# mant=input("Enter your is ntegh (Yes or No): ")
# if mant =="yes":
#     print(f"\n      ********** Oprint Toner **********")
#     print(num)
#     print(f"\n      ********** Oprint Falis ********** ")
#     print(nuu)
    
# else:
#     print("NNNO")    
    
        

#************ برنامج المهام اليومية *****************    
    
name=input("Plesae type the of the countries sepparated by a comman: ").split(", ")

#قامتين تخزن فيها المهام المنجزه والمهام التي لسئ لم تنجز
opp=[]
oop=[]

for clo in name:
    print("\n"+clo+"\n")
    num=input(f"Have you ever visited {clo} before? (yes/no)\n").lower()
    if num=='yes':
        print("I hope you had a wonderful time")
        opp.append(clo)
    else:
        print("I hope you get to visit it soon  ")
        oop.append(clo)
    print("-------------")    
    
    # قائمة التقرير للمهام
ntigh=input("Do you want to see your today's progress? (yes/no)\n").lower()
if ntigh=='yes':
    print("\n       ***** Done Tasks *****\n")
    print(opp)
    print("\n       ****** Ongoing Tasks *****\n") 
    print(oop)    

else:
    print("oo")