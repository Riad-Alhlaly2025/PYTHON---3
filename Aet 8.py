# كود لتاكيد الحضور والغياب للاسماء الموجوده في القائمة
# اذا كان الشخص موجود بيطبع تم تاكيد الحضور
# واذا كتبت له لا يعني الشخص غير موجود بيطبع لم يتم التاكيد

name=["Riad", "Ali", "Saleh"]
for num in name:
    print()
    print(num)
    nambr=input("Is this person attending ? (yas or no): ").lower()
    
    if nambr=="yas":
        print("Attendance Confirmed!")
        print("____________")
    else:
        print("Attendace not confirmed\n____________")