#مشروع عمل قائمة من نص (تطبيق على شكل لعبة تخمين من سوف يدفع الحساب)

import random   # استدعاء المكتبة العشوائيه

print("Welcome to 'whose wallet' ?")# مرحباّ بك في محفضتي
print("You will give me a list of names, and I will pick a person")
# ادخل الاسماء مع مراعاة وضع فاصله بين الاسماء

name=input("If you're ready, enter the names separated by a comma: ")
# طلب من المستخدم ادخال قائمة اسماء والكمبيوتر يطلع له اسم واحد يدفع الحساب

names=name.split(", ")
# فصل الاسماء عند وجود فاصلة بين الاسم والاسم الاخر

nam=len(names)
# عد خلاياء القائمة

num=random.randint(0,nam)-1 # -1 تعني اننا ننقص واحد بعد التوليد العشوائي لان الدالله تزيد عند العد
# اختيار عشوائي مع تحديد للداله الئ كم رقم تختار

print(f"Please ask '{names[num]}' to take his wallet out. Dinner is on him")
# طباعه ما يتم تحديده من قائمة الاسماء بعد الاختيار العشوائي