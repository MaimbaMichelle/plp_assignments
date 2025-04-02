site_name= "Maimba"
print(site_name)
site_name = "Power Learn Project"
print(site_name)

# Assigning new value to site_name
site_name = "I love coding 😊"
print(site_name)
a,b,c=5,7,"Hello world"
print(a,b,c)
num1 = 55 #numeric
num2 = 5.3
print(num1)
print(num2)  
languages = ["Python", "Dart", "Web", 23]#list
print(languages)
products = ('XBox', 499.99, "Habibi", 23)#ordered seqofitems cannot modify
print(products)
products = ('XBox', 499.99, "Habibi", 23)
print(products[2])#access
site_name = "Power Learn Project"#string
print(site_name)
student_ids = {112, 114, 117, 113}#unique
print(student_ids)
capital_city = {"Kenya": "Nairobi", "Nigeria": "Lagos"}
print(capital_city)#ordered pairs
my_list=[]
my_list=[1,"Hello",3.4]#iwth mixed data types
print(my_list[0])
print(my_list[0:])#[],2:5...
print("before append",my_list)
my_list.append(32)
print("after append",my_list)
temp=30#if
if temp>25:
    print("hot hot")
temp=20
if temp>25:
    print("hot hot")
else:
    print("chilly chilly")
temp=15
if temp>25:
    print("hot hot")
elif temp>15:
    print("warm")
else:
    print("chilly chilly")        
grade = int(input("Enter the grade: "))  # Take input as an integer

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
