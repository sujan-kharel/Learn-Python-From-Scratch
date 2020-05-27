
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

if age >= 18:
    print(name + ", You can get a driver's licence!")
elif (age >= 16) and (age <= 17):
    print(name + ", You can get a driver's license with guardian's permission!")
else:
    print(name + ", You are too young to drive!")
