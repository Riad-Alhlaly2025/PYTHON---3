#برنامج التحدي
#اولا | مرحبا بك في لعبة ضع الارنب
#رسمة 9 اشكال للعشب
#رسالة ما المكان الذي تريد الارنب الانتقال له
#طلب من المستخدم ادخال رقم السطر ورقم العمود الذي تريد الارنب الانتقال له

print("Welcome to place the rabbit\n")

nom1=['🎄', '🎄', '🎄']
nom2=['🎄', '🎄', '🎄']
nom3=['🎄', '🎄', '🎄']
print(f"{nom1}\n{nom2}\n{nom3}\n")

print("Where should the rabbit go? 🐇")
num=input("Please choose a row and a column: ")
#print(len(num))
#print(num[0])
#      العمود             الصف
if num[0]=='1' and num[1]=='1':
    print("Success ....")
    print()
    nom1.remove('🎄')
    nom1.insert(0,"🐇")
    print(f"{nom1}\n{nom2}\n{nom3}\n")
    
#      العمود             الصف    
elif num[0]=='1' and num[1]=='2':
    print("Success ....")
    print()
    nom1.remove('🎄')
    nom1.insert(1,"🐇")
    
    print(f"{nom1}\n{nom2}\n{nom3}\n")
        
        #      العمود             الصف    
elif num[0]=='1' and num[1]=='3':
    print("Success ....")
    print()
    nom1.remove('🎄')
    nom1.insert(2,"🐇")
    
    print(f"{nom1}\n{nom2}\n{nom3}\n")
    
        
#     العمود             الصف
elif num[0]=='2' and num[1]=='1':
    print("Success ....")
    print()
    nom2.remove('🎄')
    nom2.insert(0,"🐇")
    print(f"{nom1}\n{nom2}\n{nom3}\n")
    
#      العمود             الصف    
elif num[0]=='2' and num[1]=='2':
    print("Success ....")
    print()
    nom2.remove('🎄')
    nom2.insert(1,"🐇")
    
    print(f"{nom1}\n{nom2}\n{nom3}\n")
    
#      العمود             الصف    
elif num[0]=='2' and num[1]=='3':
    print("Success ....")
    print()
    nom2.remove('🎄')
    nom2.insert(2,"🐇")
    
    print(f"{nom1}\n{nom2}\n{nom3}\n")
            
            
    
    
#      العمود             الصف    
elif num[0]=='3' and num[1]=='1':
    print("Success ....")
    print()
    nom3.remove('🎄')
    nom3.insert(0,"🐇")
    
    print(f"{nom1}\n{nom2}\n{nom3}\n")
    
    #      العمود             الصف    
elif num[0]=='3' and num[1]=='2':
    print("Success ....")
    print()
    nom3.remove('🎄')
    nom3.insert(1,"🐇")
    
    print(f"{nom1}\n{nom2}\n{nom3}\n")
    
    #      العمود             الصف    
elif num[0]=='3' and num[1]=='3':
    print("Success ....")
    print()
    nom3.remove('🎄')
    nom3.insert(2,"🐇")
    
    print(f"{nom1}\n{nom2}\n{nom3}\n")
    
else:#اسف الطلب غير موجود   
    print("Sorry, the request is not available")
    
    
    
    #************************************************************
    
    #             اختصار للبرنامج الاول 
    
    #حولنا القوائم الئ سطر واحد بدلا من ثلاث قوائم
    
# # القوائم هي عباره عن سطر واحد



print("Welcome to place the rabbit")

num=[["🌳", "🌳", "🌳"], ["🌳", "🌳", "🌳"], ["🌳", "🌳", "🌳"]]
print(f"{num[0]} \n{num[1]} \n{num[2]}")    

print("Where should the rabbit go?")

name=input("Please choose a row and a column ")
on=int(name[0])
to=int(name[1])

num[on-1][to-1]="🐇"

print("\n Success ...............\n")

print(f"{num[0]} \n{num[1]} \n{num[2]}")  
