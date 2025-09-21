# كود لتاكيد الحضور والغياب للاسماء الموجوده في القائمة
# اذا كان الشخص موجود بيطبع تم تاكيد الحضور
# واذا كتبت له لا يعني الشخص غير موجود بيطبع لم يتم التاكيد

name=["Riad", "Ali", "Saleh"]
# التحقق من الاسماء كلها واحد واحد
for num in name:
    print()
    print(num)
    # هل المستخدم التالي موجود اكتب نعم
    nambr=input("Is this person attending ? (yas or no): ").lower()
    
    if nambr=="yas":
        print("Attendance Confirmed!")
        print("____________")
    else:
        print("Attendace not confirmed\n____________")
