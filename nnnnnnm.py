# name=int(input("Enter the is number :"))
# for n in range(1,11):
#     print(f"{name} * {n} = {name*n}")
#    # print(f"{name} * {n} ={name*n}")
   
names=[1,2,3,4,5]
num=0
print("Let's add each number to the next")
for n in names:
    num+=n
    
    print(f"--> {num}\n")
    print(f"The total number is :{num}")
