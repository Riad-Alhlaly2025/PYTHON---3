#split()#وضيفته يفصل شي عن شي

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
name_str=input("Enter names sparted dy a coma ..")
#طلب من المستخدم ادخال اسماء وبين كل اسم فاصله(,)

names=name_str.split(", ")
#الداله تفصل عندما تجد الفاصله كوما


print(type(names))
print(names)
print(len(names))
