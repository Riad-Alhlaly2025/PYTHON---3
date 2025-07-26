
#مرحبا بك في محفضة وايت؟
#Welcome to 'whose wallet?'
#ادخل قائمة اسماء لكي اختار احد منهم يدفع الحساب
#You will give me a list of names, and I will pick a person to pay If you're ready, enter the names separated by a comma:

#يكون الاختيار عشوائي

#الرجاء اطلب من علي يطلع محفضتة يدفع الحساب
#Please ask 'Ali' to take his wallet out. Dinner is on him

import random

print("Welcome to 'whose wallet?'")
num=input("You will give me a list of names, and I will pick a person to pay If you're ready, enter the names separated by a comma:\n")

#|||||||||||||||||||||||||||||||||||||||
nume=num.split(", ")

n=len(nume)-1

nu=random.randint(0,n)

k=nume[n]
print(f"Please ask '{k}' to take his wallet out. Dinner is on him")
#|||||||||||||||||||||||||||||||||||||||

#كود مختصر لكل الي بين المربع الخطوط 
print(f"Please ask {random.choice(num)} to take out his wallet, dinner is on him.")


#.....................................................................
#*****كود حديد مختصر الاسطور ******
#[
import random
print("Welcome to 'whose wallet?")
print(f"Please ask {random.choice(input('Enter the names seaparated by a comma :  ').split(', ')) } to take out his wallet. Dinner is on him! ")
#]
#............................................................................