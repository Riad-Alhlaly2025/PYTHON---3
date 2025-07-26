

#***************** (مشروع عبارة عن منشاء كلمات مرور\سر قوية جداً) ************************

# استدعاء المكتبة الارقام العشوائية ومكتبة تكوين النص العشوائي
import random
import string

# رسالة \ مرحباء بك في منشاء كلمات السر
print("Welcome to the Password Generatoe!")

# طلب من المستخدم ادخال البيانات لكلمة السر حسب الطلب
#* عدد خانات كلمة السر
number=int(input("Enter the total number of characters in the password: "))
#* عدد الحروف التي تريدها في كلمة السر 
letter=int(input("Enter the number of letters in password: "))
#* عدد الارقام التي تريدها في كلمة السر
numbers=int(input("Enter the number of numbers in the password: "))
#* عدد الرموز المختلفه التي تريدها في كلمة السر
symbols=int(input("Enter the number of symbols in the password: "))

# جمع الارقام التي ادخلها المستخدم لكي اتحقق هل هي اصغر او تساوي حجم كلمة المرور التي اختاره
sums=int(letter+numbers+symbols)

# التحقق اذا كان الرقم الذي اختاره اولاُ اكبر او يساوي مجموع عدد الذي ادخله لانشاء كلمة المرور ينفذ الشرط
if number >= sums:
    
    on1=random.choices(string.ascii_letters,k=letter)
    to2=random.choices(string.digits,k=numbers)
    thre3=random.choices(string.punctuation,k=symbols)
        
    # نجمع العناصر مع بعض    
    clo=on1+to2+thre3
    # نخلط العناصر عشوائي مع بعضها البعض
    random.shuffle(clo)
    
    #طباعه كلمة المرور مع ازالة المسافات التي بين عناصر كلمة المرور
    print(f"Generated Password: "+"".join(clo))
    
# اذا لم يتحقق الشرط تطبع له هاذه الرساله    
else:
    print("Invalid input. The sum of letters, number, and symbols doesn't match the password")

#**************************************(النهاية)*************************************************




#****** شروحات بسيطه لتسهيل عمل مشروع الموجود اعلى  *********************************************




#** كود يرتب الكمله الغير مفهومه اول مشعبكه مع رموز ************************

# import string
# name=input("Please type a sentence: ")
# num=" "
# for x in  name:
#     if x not in string.punctuation:
#         num += x
        
# print("\n \n *** Here is the same sentence without punctuation***\n"+num)        


# #** لكي اختار مجموعه من الاختيارات العشوائيه استخدم التالي
# #* لاختيار 5 حروف نص عشوائيه من كبتيل وسمول استخدم التالي
# import random
# import string
# number_5=random.choices(string.ascii_letters,k=4)
# print(number_5)
#****************************************************


# #*** لكي الخبط نص او قائمة فيها عناصر استخدم التالي *******
# #***  random.shuffle(المطلوب لخبطتة) *********
# enter=[1,2,3,4,5,6,7,8,9]
# random.shuffle(enter)
# print(enter)
