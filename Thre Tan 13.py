
#*1** (Slicing - التشريح) استخدام ال 
name =["Riad", "Ali", "Saleh", "Ahmed", "Mruaan", "Khaleed", "Saif", "Naseer"]
print(name[1:9:2])
print(name[1:3])# اطبع من اول عنصر الى ثالث عنصر فقط



#*2**** (الجمله الشرطيه داخل التكرار) استخدام ال 
name =["Riad", "Ali", "Saleh", "Ahmed", "Mruaan", "Khaleed", "Saif", "Naseer"]
for n in name:
    print(n)
    
    if n==name[3]:
        break
    
    
    #*3***** (Join) استخدام ال ********
name =["Riad", "Ali", "Saleh", "Ahmed", "Mruaan", "Khaleed", "Saif", "Naseer"]
print("\n".join(name))





#*4***(Range()) استخدام ال **********
for n in range(0,5,3):
    print(n)



#*5*** لتخزين في قائمة وتفكيك العناصر عن بعضها البعض (Split()) استخدام ال *****
name=input("ادخل اسماء الطلاب وضع فاصله بين كل اسم")
print(name.split(", "))
        