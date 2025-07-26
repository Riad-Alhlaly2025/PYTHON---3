#  (range()) ثلاث طرق لاستخدام 

#1) اطبع الى عشره
for i in range(10):
    print(i)
    
#2) اطبع من الرقم المحدد له في الخانه الاولئ الئ الرقم المحدد له في الخانه الثانيه    
for i in range(1, 10):
    print(i)

#3) اطبع من الرقم واحد الى مئة وعند طباعة تخطئ كل عشر خطوات
for i in range(1,100, 10):
    print(i)
 
 
#***********************************************
    
#    جدول ضرب لحاصل رقم واحد يقوم بادخاله المستخدم الى 10
print("*** Welcome to the multiplication table ***")
numpr=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{numpr} * {i} = {numpr*i}")
        
