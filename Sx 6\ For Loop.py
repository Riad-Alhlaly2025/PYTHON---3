# برنامج يطلب من المستخدم ادخال كلمة سر
# يوجد ثلاث محاولات للمستخدم فقط

print("Welcome")
# ترحيب

num="1234"
# كلمة السر

for i in range(3):
    #عملية التكرار للمحاولات الثلاثة
    
    opp=input("Enter pasuord: ")
    # طلب من المستخدم ادخال كلمة السر المطلوبه
    
    print(i)
    if opp==num:
        print("You mrhpa")
        break
  
